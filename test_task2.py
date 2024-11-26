import unittest
from task2 import calculate_total_cost_with_tax

class TestCalculateTotalCostWithTax(unittest.TestCase):
    def setUp(self):
        self.prices = {
            'tshirt': 0.5,
            'socks': 0.3,
            'jacket': 0.8
        }
        self.tax_rate = 0.1  # 10% tax

    def test_calculate_total_cost_with_tax(self):
        items_bought = ['tshirt', 'socks', 'jacket', 'socks']
        expected_total = (0.5 + 0.3 + 0.8 + 0.3) * 1.1  # Including 10% tax
        self.assertEqual(calculate_total_cost_with_tax(self.prices, items_bought, self.tax_rate), expected_total)

    def test_calculate_total_cost_with_missing_items(self):
        items_bought = ['tshirt', 'socks', 'jewerly']  # 'jewerly' is not in prices
        expected_total = (0.5 + 0.3) * 1.1  # Including 10% tax
        self.assertEqual(calculate_total_cost_with_tax(self.prices, items_bought, self.tax_rate), expected_total)

if __name__ == '__main__':
    unittest.main()