#4 find the missing num in consecutive array

def find_missing_number(arr):
    n = len(arr) + 1
    total_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return total_sum - actual_sum

# Example usage:
print(find_missing_number([1, 2, 3, 5]))  # Output: 4
