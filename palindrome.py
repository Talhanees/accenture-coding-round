#3 function to check if the given string is palindrome

def is_palindrome(s):
    return s == s[::-1]

# Example usage:
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False
