def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

# # Example usage
# print(is_palindrome("A man, a plan, a canal: Panama"))  # True
# print(is_palindrome("race a car"))  # False
# # Example usage 
# print(is_palindrome("No 'x' in Nixon"))  # True
input_str = input("Enter a string to check if it's a palindrome: ")
print(is_palindrome(input_str))
