def is_palindrome(s):
    return s.lower() == s.lower()[::-1]


print(is_palindrome("Abba"))
