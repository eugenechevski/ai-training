from collections import defaultdict

def process_sales_data(transactions):
    """
    Filters out transactions with negative amounts,
    aggregates sales by product category,
    and returns a summary of total sales per category.
    Args:
        transactions (list): List of sales transactions as dictionaries.
    Returns:
        dict: Summary of total sales per category.
    """
    sales_data = defaultdict(int)

    # Filter out negative amount transactions and aggregate sales per category.
    for transaction in transactions:
        if transaction['amount'] > 0:
            category = transaction['category']
            sales_data[category] += transaction['amount']

    return dict(sales_data)
    
# Example usage:    
transactions = [
    {'category': 'Books', 'amount': 12.50},
    {'category': 'Stationery', 'amount': 8.99},
    {'category': 'Books', 'amount': 29.99},
    {'category': 'Electronics', 'amount': -7.85},  # Negative amount, will be filtered out
    {'category': 'Stationery', 'amount': 6.75},
    {'category': 'Toys', 'amount': 34.95}
] 
result = process_sales_data(transactions)
print(result)