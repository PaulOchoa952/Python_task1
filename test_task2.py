import unittest
from task2 import calculate_total_cost_with_tax

#class to test the function calculate_total_cost_with_tax
class TestCalculateTotalCostWithTax(unittest.TestCase):
    
    def setUp(self):

        # Set up the prices and tax rate for the test cases
        self.prices = {
            'socks': 5,
            'shoes': 60,
            'sweater': 30
        }
        self.tax_rate = 0.1  # 10% tax

    #test case to check the total cost of items bought including tax
    def test_calculate_total_cost_with_tax(self):
        items_bought = ['socks', 'shoes', 'socks']
        total_cost = sum(self.prices[item] for item in items_bought if item in self.prices)
        expected_total = round(total_cost * (1 + self.tax_rate), 2)  # Including 10% tax and rounding to 2 decimal places
        self.assertEqual(calculate_total_cost_with_tax(self.prices, items_bought, self.tax_rate), expected_total)

    #test case to check the total cost of items bought including tax with missing items
    def test_calculate_total_cost_with_missing_items(self):
        items_bought = ['socks', 'shoes', 'jewelry']  # 'jewelry' is not in prices
        total_cost = sum(self.prices[item] for item in items_bought if item in self.prices)
        expected_total = round(total_cost * (1 + self.tax_rate), 2)  # Including 10% tax and rounding to 2 decimal places
        self.assertEqual(calculate_total_cost_with_tax(self.prices, items_bought, self.tax_rate), expected_total)

if __name__ == '__main__':
    unittest.main()