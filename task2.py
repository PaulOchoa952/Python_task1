
def calculate_total_cost_with_tax(prices: dict[str, float], items_bought: list[str], tax_rate: float) -> float:
    """
    Calculates the total cost of items bought including tax.

    :param prices: Dictionary with item names as keys and their costs as values.
    :param items_bought: List of item names that were bought.
    :param tax_rate: Tax rate to be applied to the total cost.
    :return: Total cost of the items bought including tax.
    """
    total_cost = 0.0
    #for each item in items_bought, if the item is in prices, add the price to total_cost
    for item in items_bought:
        if item in prices:
            total_cost += prices[item]
    total_cost_with_tax = total_cost * (1 + tax_rate)

    #round the total_cost_with_tax to 2 decimal places
    return round(total_cost_with_tax,2)

def main():
    #dictionary with item names as keys and their costs as values
    prices = {
        'socks': 5,
        'shoes': 60,
        'sweater': 30
    }

    tax_rate = 0.09  # 10% tax

    #list of item names that were bought
    items_bought = ['socks', 'shoes']
    total_cost = calculate_total_cost_with_tax(prices, items_bought, tax_rate)
    print(f"Total cost including tax: {total_cost}")
    
    #list of item names that were bought with missing items
    items_bought = ['tshirt', 'socks', 'jewerly']  # 'jewerly' is not in prices
    total_cost = calculate_total_cost_with_tax(prices, items_bought, tax_rate)
    print(f"Total cost including tax: {total_cost}")

if __name__ == "__main__":
    main()