def simulate_trading(stock_prices):
    max_profit = 0
    for buy_index in range(len(stock_prices)-1):
        for sell_index in range(buy_index+1, len(stock_prices)):
            potential_profit = stock_prices[sell_index] - stock_prices[buy_index]
            max_profit = max(max_profit, potential_profit)

    return max_profit

#Example usage:
sample_prices = [10, 7, 5, 8, 11, 9]
profit = simulate_trading(sample_prices)
print(profit) #Output : 4


def simulate_trading(stock_prices):
    min_price = float('inf')
    max_profit = 0

    for price in stock_prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    
    return max_profit if max_profit > 0 else 0       
   
#Example usage:        
sample_prices = [10, 7, 5, 8, 11, 9]
profit = simulate_trading(sample_prices)
print(profit) #Output : 4