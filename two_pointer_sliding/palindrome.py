"""
Docstring for two_pointer_sliding.palindrome
Example 1: Given a string s, return true if it is a palindrome, false otherwise.

A string is a palindrome if it reads the same forward as backward. That means, after reversing it, it is still the same string. For example: “abcdcba”, or “racecar”.
"""


def is_palindrome(sting: str) -> bool:
    left = 0
    right_pointer = len(sting) - 1

    while left < right_pointer:
        if sting[left].lower() != sting[right_pointer].lower():
            return False
        left += 1
        right_pointer -= 1
    return True


if __name__ == "__main__":
    res = is_palindrome("raceCar")
    print(res)
