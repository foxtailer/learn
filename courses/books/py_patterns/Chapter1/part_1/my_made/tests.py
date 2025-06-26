import unittest

from made import *


class TestProduct(unittest.TestCase):

    def test_product_proper_init(self):
        product = Product('Red Chair')
        self.assertEqual(product.SKU, 'Red Chair')


class TestBatches(unittest.TestCase):

    def test_batche_check_product(self):
        batche = Batche([
            ['Red Chair', 3],
            ['Blue Chair', 2]
            ])

        self.assertTrue(batche.check_product('Red Chair', 3))
        self.assertFalse(batche.check_product('Blue Chair', 3))
        self.assertFalse(batche.check_product('Yellow Chair', 1))


if __name__ == '__main__':
    unittest.main()
