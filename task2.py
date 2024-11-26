
def calculate_total_cost_with_tax(prices: dict[str, float], items_bought: list[str], tax_rate: float) -> float:
    """
    Calculates the total cost of items bought including tax.

    :param prices: Dictionary with item names as keys and their costs as values.
    :param items_bought: List of item names that were bought.
    :param tax_rate: Tax rate to be applied to the total cost.
    :return: Total cost of the items bought including tax.
    """
    total_cost = 0.0
    
    for item in items_bought:
        if item in prices:
            total_cost += prices[item]
    total_cost_with_tax = total_cost * (1 + tax_rate)

    return total_cost_with_tax