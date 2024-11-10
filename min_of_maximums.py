from collections import deque

def min_of_maximums(arr, n, k):
    dq = deque()  # Deque to store indices of array elements
    max_values = []

    # Process the first k elements to fill the deque
    for i in range(k):
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()
        dq.append(i)

    # Record the maximum for the first window
    max_values.append(arr[dq[0]])

    # Process the rest of the array
    for i in range(k, n):
        # Remove elements out of the current window from the deque
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Remove elements smaller than the current element
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()

        dq.append(i)

        # Append the maximum of the current window
        max_values.append(arr[dq[0]])

    # Return the minimum of the maximums from all windows
    return min(max_values)


# Input
arr = [3, 1, 4, 1, 5, 9]  # Array elements
n = len(arr)               # Size of the array
k = 2                      # Length of the segment (window)

# Output with empty lines before printing the result
print("\n" * 2)
print(min_of_maximums(arr, n, k))
