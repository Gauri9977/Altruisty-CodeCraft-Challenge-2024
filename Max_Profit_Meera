### Problem Statement:

Meera is a real estate investor who buys properties at a low price and sells them at a higher price to maximize her profit. If prices only decrease, she doesn't buy. Your task is to calculate the maximum profit Meera could have made based on the daily property prices.

---

### Approach:

To find the maximum profit, we track the lowest price seen so far and calculate the potential profit at each step. The result is the maximum of these profits.

---

### Code Implementation:

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

---

### Explanation:

- We initialize `min_price` to infinity and `max_profit` to 0.
- For each price, we update `min_price` and calculate the potential profit (`price - min_price`), updating `max_profit` if needed.
- Finally, we print the `max_profit`.

---

### Time Complexity:
- **O(n)**: We iterate over the list of prices once.

### Space Complexity:
- **O(n)**: Space for storing prices.

---

This is an efficient and short solution for calculating the maximum profit Meera can make.
