def max_profit(n, prices):
    if n < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit

# Read input in the specified format
raw_input = input()
n, prices = eval(raw_input)

# Call the function and print the result
print(max_profit(n, prices))
