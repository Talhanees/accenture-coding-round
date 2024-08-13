#5 find the common elements from both array

def find_common_elements(arr1, arr2):
    return list(set(arr1) & set(arr2))

# Example usage:
print(find_common_elements([1, 2, 3, 4], [3, 4, 5, 6]))  # Output: [3, 4]
