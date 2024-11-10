# Altruisty CodeCraft Challenge 2024 🚀

Welcome to my **Altruisty CodeCraft Challenge** repository! Here, you'll find my solutions to the coding challenges of the competition. 🖥️

### 📚 Challenge Breakdown:
1. **Coding Challenge**: 5 unique problems solved with code.

## How I Participated 📝

I participated in the **Coding Challenge** 🖥️ and submitted solutions to 5 coding problems. This repo contains the code implementations 🧑‍💻.

---

Q. 1.
### Problem Statement:

Meera is a real estate investor who buys properties at a low price and sells them at a higher price to maximize her profit. If prices only decrease, she doesn't buy. Your task is to calculate the maximum profit Meera could have made based on the daily property prices.


### Approach:

To find the maximum profit, we track the lowest price seen so far and calculate the potential profit at each step. The result is the maximum of these profits.


### Explanation:

- We initialize `min_price` to infinity and `max_profit` to 0.
- For each price, we update `min_price` and calculate the potential profit (`price - min_price`), updating `max_profit` if needed.
- Finally, we print the `max_profit`.


### Time Complexity:
- **O(n)**: We iterate over the list of prices once.

### Space Complexity:
- **O(n)**: Space for storing prices.

---

Q. 2. 
### Problem Statement:

In a given string representing a line segment with bees (`*`) and flowers (`|`), you are tasked to calculate the number of bees between two flowers for each given range of indices. The indices are 1-indexed.


### Approach:

1. **Prefix Sum**: Create a prefix sum array to count the bees (`*`) up to each index.
2. **Process Queries**: For each query, find the first and last flowers (`|`) in the range, and count the bees between them using the prefix sum.


### Explanation:

- **Prefix Sum Array**: We calculate the cumulative number of bees up to each index in the string.
- **Query Processing**: For each query, we find the first and last flowers in the specified range and use the prefix sum to count the bees between them.
- **Edge Cases**: If no valid pair of flowers is found in the range, we append 0 to the result.


### Time Complexity:

- **O(n)**: Calculating the prefix sum.
- **O(q)**: Processing each query, where `q` is the number of queries.

### Space Complexity:

- **O(n)**: Storing the prefix sum array.

---

Q. 3.
# Problem Statement:

Given an array, find the minimum of the maximums of all contiguous subarrays of length `k`.

### Input:

- `k` : Length of the subarray.
- `n` : Size of the array.
- `arr[]` : Array of size `n`.

### Output:
Return the minimum of the maximums of all contiguous subarrays of size `k`.


### Explanation:

- The sliding window approach uses a deque to find the maximum in each window.
- The result is the minimum of these maximums.

### Time Complexity:
- **O(n)**: Each element is processed once.

### Space Complexity:
- **O(k)**: The deque stores up to `k` elements.

---

Q. 4. 
### Problem Statement

You are given a list of candy flavours with their counts. Your task is to find the first flavour that appears an odd number of times. If all flavours appear an even number of times, output "All are even."

### Input:
- The first line contains an integer \( N \) (3 ≤ N ≤ 50), the number of flavours.
- The next \( N \) lines contain the flavours as strings.

### Output:
- A single string representing the first flavour that appears an odd number of times, or "All are even" if no flavour has an odd count.

### Time Complexity:
- **O(N)**: We count the occurrences of flavours using `Counter`, which takes linear time.

### Space Complexity:
- **O(N)**: We store the count of each flavour in a `Counter`, requiring space proportional to the number of flavours.

---

Q. 5.
### Problem Statement

You are tasked with determining the strongest trainee(s) from a group of 4 trainees based on their strength test results over 3 rounds. You will calculate the average strength level for each trainee across the 3 rounds and identify the strongest trainee(s). If there are multiple trainees with the highest average, all should be selected. If the highest average is below 100, the trainees are considered unfit.

### Input:
- 12 integer values representing strength levels for each trainee in each round.
- The values are recorded as:
  - Round 1: Strength level of Trainee 1, Trainee 2, Trainee 3, Trainee 4.
  - Round 2: Strength level of Trainee 1, Trainee 2, Trainee 3, Trainee 4.
  - Round 3: Strength level of Trainee 1, Trainee 2, Trainee 3, Trainee 4.

### Output:
- Trainee(s) with the highest average strength level, listed by their trainee number.
- If any input strength level is outside the range 1 to 200, output "INVALID INPUT".
- If all trainees' highest average strength level is below 100, output "All trainees are unfit".

#### Explanation:
From the input, the strength levels for each trainee are:
- Trainee 1: [150, 140, 160], average = 150
- Trainee 2: [160, 130, 135], average = 142
- Trainee 3: [155, 125, 125], average = 135
- Trainee 4: [158, 142, 140], average = 146

The highest average strength is 150 (Trainee 1), followed by 146 (Trainee 4), but since there are multiple trainees with the highest average (Trainee 1 and Trainee 3), they are both selected.

### Time Complexity:
- **O(1)**: Since the number of trainees and rounds is fixed, the computation involves only basic arithmetic operations.

### Space Complexity:
- **O(1)**: We only need a constant amount of space to store the input and compute averages.

---
