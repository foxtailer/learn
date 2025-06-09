import unittest

from model import *
from datetime import date, timedelta


class TestAllocateDomainService(unittest.TestCase):
    def setUp(self):
        self.today = date.today()
        self.tomorrow = self.today + timedelta(days=1)
        self.later = self.today + timedelta(days=10)

    def test_prefers_current_stock_batches_to_shipments(self):
        in_stock_batch = Batch("in-stock-batch", "RETRO-CLOCK", 100,
                                eta=None)
        shipment_batch = Batch("shipment-batch", "RETRO-CLOCK", 100,
                                eta=self.tomorrow)
        line = OrderLine("oref", "RETRO-CLOCK", 10)
        allocate(line, [in_stock_batch, shipment_batch])

        assert in_stock_batch.available_quantity == 90
        assert shipment_batch.available_quantity == 100

    def test_prefers_earlier_batches(self):
        earliest = Batch("speedy-batch", "MINIMALIST-SPOON", 100,
                         eta=self.today)
        medium = Batch("normal-batch", "MINIMALIST-SPOON", 100,
                        eta=self.tomorrow)
        latest = Batch("slow-batch", "MINIMALIST-SPOON", 100, eta=self.later)
        line = OrderLine("order1", "MINIMALIST-SPOON", 10)
        allocate(line, [medium, earliest, latest])

        assert earliest.available_quantity == 90
        assert medium.available_quantity == 100
        assert latest.available_quantity == 100

    def test_returns_allocated_batch_ref(self):
        in_stock_batch = Batch("in-stock-batch-ref", "HIGHBROW-POSTER",
                                100, eta=None)
        shipment_batch = Batch("shipment-batch-ref", "HIGHBROW-POSTER",
                                100, eta=self.tomorrow)
        line = OrderLine("oref", "HIGHBROW-POSTER", 10)
        allocation = allocate(line, [in_stock_batch, shipment_batch])

        assert allocation == in_stock_batch.reference

    def test_raises_out_of_stock_exception_if_cannot_allocate(self):
        batch = Batch('batch1', 'SMALL-FORK', 10, eta=self.today)
        allocate(OrderLine('order1', 'SMALL-FORK', 10), [batch])

        with self.assertRaises(OutOfStock) as cm:
            allocate(OrderLine('order2', 'SMALL-FORK', 1), [batch])
            self.assertIn('SMALL-FORK', str(cm.exception))


if __name__ == '__main__':
    unittest.main()
