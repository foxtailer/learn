from datetime import date

from their_made.domain.model import Batch, OrderLine
from their_made.types import OrderLineSchema, BatchSchema


def make_batch_and_line(sku, batch_qty, line_qty):
    batch_data = {
        'sku': sku,
        'eta': date.today(),
        'qty': batch_qty,
    }
    
    line_data = {
        'sku': sku,
        'qty': line_qty,
    }

    batch_shema = BatchSchema.model_validate(batch_data)
    line_shema = OrderLineSchema.model_validate(line_data)

    return (
        Batch(
            batch_shema.reference,
            batch_shema.sku,
            batch_shema.qty,
            batch_shema.eta,
        ),

        OrderLine(
            line_shema.orderid,
            line_shema.sku,
            line_shema.qty,
        )
    )


def test_allocating_to_a_batch_reduces_the_available_quantity():
    batch, line = make_batch_and_line('ELEGANT-LAMP', 20, 2)
    batch.allocate(line)
    
    assert batch.available_quantity == 18


def test_can_allocate_if_available_greater_than_required():
    large_batch, small_line = make_batch_and_line("ELEGANT-LAMP", 20, 2)

    assert large_batch.can_allocate(small_line)


def test_cannot_allocate_if_available_smaller_than_required():
    small_batch, large_line = make_batch_and_line("ELEGANT-LAMP", 2, 20)

    assert not small_batch.can_allocate(large_line)


def test_can_allocate_if_available_equal_to_required():
    batch, line = make_batch_and_line("ELEGANT-LAMP", 2, 2)

    assert batch.can_allocate(line)


def test_cannot_allocate_if_skus_do_not_match():
    batch = Batch("batch-001", "UNCOMFORTABLE-CHAIR", 100, eta=None)
    different_sku_line = OrderLine("order-123", "EXPENSIVE-TOASTER", 10)

    assert batch.can_allocate(different_sku_line) is False


def test_allocation_is_idempotent():
    batch, line = make_batch_and_line("ANGULAR-DESK", 20, 2)
    batch.allocate(line)
    batch.allocate(line)

    assert batch.available_quantity == 18


def test_deallocate():
    batch, line = make_batch_and_line("EXPENSIVE-FOOTSTOOL", 20, 2)
    batch.allocate(line)
    batch.deallocate(line)

    assert batch.available_quantity == 20


def test_can_only_deallocate_allocated_lines():
    batch, unallocated_line = make_batch_and_line("DECORATIVE-TRINKET", 20, 2)
    batch.deallocate(unallocated_line)
    
    assert batch.available_quantity == 20
