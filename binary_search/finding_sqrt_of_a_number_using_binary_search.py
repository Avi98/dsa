"""
Problem Statement: You are given a positive integer n.
Your task is to find and return its square root.
If ‘n’ is not a perfect square, then return the floor value of sqrt(n).

Input: N = 36
Output: 6
Explanation: Square root of 36 is 6.
Input: N = 28
Output: 5
Explanation: Square root of 28 is approximately 5.292. So, the floor value will be 5.

"""

import math


def finding_sqrt(num: int):
    low = 1
    high = num

    while low < high:
        mid = math.ceil((low + high) / 2)

        print(f"mid is:{mid} and root is {2} ")

        if mid * mid == num:
            return mid

        if mid * mid < num:
            low = mid
        else:
            high = mid - 1
    # return -1


if __name__ == "__main__":
    x = finding_sqrt(36)
    print(f"Square root is:{x}")
