from collections import Counter

def first_odd_flavour(N, C):
    flavour_count = Counter(C)
    
    # Iterate through the flavours in the order they appear in the list
    for flavour in C:
        if flavour_count[flavour] % 2 != 0:
            return flavour
    return "All are even"

# Input
N = int(input())  # Number of flavours
C = [input().strip() for _ in range(N)]  # List of flavours

# Output with empty lines before result
print("\n" * 2)
print(first_odd_flavour(N, C))
