import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from sqlalchemy import text

from model import OrderLine
from orm import metadata, start_mappers


class TestOrderLineMapper(unittest.TestCase):
    def setUp(self):
        # In-memory SQLite DB for testing
        self.engine = create_engine('sqlite:///:memory:')
        metadata.create_all(self.engine)
        start_mappers()
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def tearDown(self):
        self.session.close()
        clear_mappers()

    def test_orderline_mapper_can_load_lines(self):
        self.session.execute(text(
                'INSERT INTO order_lines (orderid, sku, qty) VALUES '
                '("order1", "RED-CHAIR", 12),'
                '("order1", "RED-TABLE", 13),'
                '("order2", "BLUE-LIPSTICK", 14)'
            )
        )
        self.session.commit()

        expected = [
            OrderLine("order1", "RED-CHAIR", 12),
            OrderLine("order1", "RED-TABLE", 13),
            OrderLine("order2", "BLUE-LIPSTICK", 14),
        ]

        result = self.session.query(OrderLine).all()
        self.assertEqual(result, expected)

    def test_orderline_mapper_can_save_lines(self):
        new_line = OrderLine("order1", "DECORATIVE-WIDGET", 12)
        self.session.add(new_line)
        self.session.commit()

        rows = list(self.session.execute(
            text('SELECT orderid, sku, qty FROM order_lines')
        ))

        self.assertEqual(rows, [("order1", "DECORATIVE-WIDGET", 12)])


if __name__ == '__main__':
    unittest.main()
