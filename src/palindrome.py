def is_palindrome(input: str) -> bool:
    test = input[::-1]
    return test == input
