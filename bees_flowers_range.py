def count_bees_between_flowers(s, startIndex, endIndex):
    # Length of the string
    n = len(s)
    
    # Prefix sum array to store count of bees (`*`) up to each index
    prefixBeeCount = [0] * (n + 1)
    
    # Build the prefix sum array
    for i in range(1, n + 1):
        prefixBeeCount[i] = prefixBeeCount[i - 1] + (1 if s[i - 1] == '*' else 0)
    
    # Result list to store answers for each query
    result = []
    
    # Iterate over each query and process
    for start, end in zip(startIndex, endIndex):
        # Adjust to 0-based index
        start -= 1
        end -= 1
        
        # Find the positions of the first and last flowers ('|') in the range
        flower_count = 0
        first_flower = -1
        last_flower = -1
        for i in range(start, end + 1):
            if s[i] == '|':
                flower_count += 1
                if flower_count == 1:
                    first_flower = i
                elif flower_count == 2:
                    last_flower = i
                    break
        
        # If we found two flowers in the range
        if flower_count == 2:
            # Count the bees between the two flowers
            bees_in_range = prefixBeeCount[last_flower + 1] - prefixBeeCount[first_flower]
            result.append(bees_in_range)
        else:
            result.append(0)  # No valid bees between two flowers
    
    return result

# Input Parsing
s = input()  # Read string s
n = int(input())  # Number of startIndex values
startIndex = [int(input()) for _ in range(n)]  # Start indices
m = int(input())  # Number of endIndex values
endIndex = [int(input()) for _ in range(m)]  # End indices

# Call the function and output the results
result = count_bees_between_flowers(s, startIndex, endIndex)

# Adding empty lines before output
print("\n")

# Print the result for each query
print(*result)  # Print the result for each query
