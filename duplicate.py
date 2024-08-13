#6 removing the dulicates elements while peservering the order

def remove_duplicates(arr):
    seen = set()
    result = []
    for item in arr:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4, 1, 5]))  # Output: [1, 2, 3, 4, 5]
