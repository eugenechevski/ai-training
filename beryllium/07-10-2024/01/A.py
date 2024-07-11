def calculate_max_profit(stock_prices):
    max_profit = 0
    for i in range(len(stock_prices)-1):
        if stock_prices[i+1] > stock_prices[i]:
            potential_profit = stock_prices[i+1] - stock_prices[i]
            if potential_profit > max_profit:
                max_profit = potential_profit
    return max_profit

stock_prices = [100, 80, 120, 150, 90, 70]
max_profit = calculate_max_profit(stock_prices)
print("Maximum profit:", max_profit)