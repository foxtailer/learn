'''
модель предметной области | Buisness logic | Mid layer in onion architecture
Domain model for MADE.com
'''
# Модель предметной области — это мысленный образ бизнеса.
# Behavior determinate db requirements

import typing
from dataclasses import dataclass
from datetime import date

'''
Продукт идентифицируется по артикулу, или единице складского учета (stock-
keeping unit, SKU). Клиенты (customers) делают заказы (orders). Заказ иденти-
фицируется ссылкой на заказ (order reference) и состоит из нескольких товарных
позиций, или строк (order lines), где каждая товарная позиция имеет артикул
и количество (quantity). Например:
y 10 шт. артикула СТУЛ-КРАСНЫЙ;
y 1 шт. артикула ЛАМПА-БЕЗВКУСНАЯ.
Отдел закупок заказывает малые партии (batches) товара. Партия товара имеет
уникальный идентификатор, именуемый ссылкой, артикулом и количеством.
Нужно разместить товарные позиции заказа (allocate order lines) в партиях товара.
После того как мы это сделали, мы отправляем товар из этой конкретной партии
на клиентский адрес доставки. Когда мы размещаем x штук в партии товара, то
его располагаемое количество (available quantity) уменьшается на x. Например:
y у нас есть партия из 20 шт. артикула СТОЛ-МАЛЫЙ, и мы размещаем в ней
товарную позицию на 2 шт. артикула СТОЛ-МАЛЫЙ;
y в партии товара должно остаться 18 шт. артикула СТОЛ-МАЛЫЙ.
Мы не можем размещать товарные позиции заказа, если располагаемое количество
меньше количества в товарной позиции. Например:
y у нас есть партия из 1 шт. артикула ПОДУШКА-СИНЯЯ и товарная позиция
на 2 шт. артикула ПОДУШКА-СИНЯЯ;
y мы не можем разместить эту позицию в партии товара.
Мы не можем размещать одну и ту же товарную позицию заказа дважды. Например:
y у нас есть партия из 10 шт. артикула ВАЗА-СИНЯЯ, и мы размещаем товарную
позицию на 2 шт. артикула ВАЗА-СИНЯЯ;
y если снова разместить эту позицию в той же партии товара, то указанная партия
все равно должна иметь количество 8 шт.
Партии товара имеют предполагаемый срок прибытия (estimated arrival time, ETA),
если они в настоящее время в пути, либо они могут быть на складе (warehouse stock).
Складские партии имеют приоритет в размещении. Приоритет партий в пути за-
висит от их предполагаемого срока прибытия — чем раньше срок, тем более партия
приоритетна к размещению.
'''


class OutOfStock(Exception):
    pass


@dataclass(unsafe_hash=True)
class OrderLine:
    '''
    Orders consist of n order lines
    '''
    orderid: str
    sku: str  # stock-keeping unit / product id
    qty: int


class Batch:
    """
    партии товара от поставщика
    """
    def __init__(
            self, ref: str, sku: str, qty: int, eta: typing.Optional[date]
        ):
        self.reference = ref
        self.sku = sku
        self.eta = eta
        self._purchased_quantity = qty
        self._allocations = set() # тип 'множество': Set[OrderLine]

    def __eq__(self, other):
        if not isinstance(other, Batch):
            return False
        return other.reference == self.reference
    
    def __hash__(self):
        return hash(self.reference)
    
    def __gt__(self, other):
        if self.eta is None:
            return False
        if other.eta is None:
            return True
        return self.eta > other.eta

    def allocate(self, line: OrderLine):
        if self.can_allocate(line):
            self._allocations.add(line)

    def can_allocate(self, line: OrderLine) -> bool:
        return self.sku == line.sku and self.available_quantity >= line.qty
    
    @property
    def allocated_quantity(self) -> int:
        return sum(line.qty for line in self._allocations)

    @property
    def available_quantity(self) -> int:
        return self._purchased_quantity - self.allocated_quantity

    def deallocate(self, line: OrderLine):
        if line in self._allocations:
            self._allocations.remove(line)


def allocate(line: OrderLine, batches: list[Batch]) -> str:
    try:
        batch = next(
             b for b in sorted(batches) if b.can_allocate(line)
        )
        batch.allocate(line)
        return batch.reference

    except StopIteration:
        raise OutOfStock(f'Артикула {line.sku} нет в наличии')
