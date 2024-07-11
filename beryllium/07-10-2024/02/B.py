from collections import defaultdict

def process_sales_data(transactions):
    """
    Filters out transactions with negative amounts,
    aggregates sales by product category
    and returns a summary of total sales per category.

    :param transactions: List of sales transactions as dictionaries.
    :type transactions: list[dict]
    :return: Dictionary with product categories and their total sales.
    :rtype: dict
    """
    sales_by_category = defaultdict(int)

    # Filter out negative sales and aggregate sales per category
    for transaction in transactions:
        if transaction['amount'] > 0:
            category = transaction['category']
            sales_by_category[category] += transaction['amount']

    return dict(sales_by_category)

# Example usage:
transactions = [
    {'category': 'Books', 'amount': 12.49},
    {'category': 'Stationery', 'amount': 8.99},
    {'category': 'Books', 'amount': 29.99},
    {'category': 'Electronics', 'amount': -7.00},  # Negative amount, will be filtered out
    {'category': 'Stationery', 'amount': 6.95},
]  
result = process_sales_data(transactions)
print(result)