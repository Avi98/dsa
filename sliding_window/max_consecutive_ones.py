"""
https://takeuforward.org/data-structure/max-consecutive-ones-iii
Docstring for sliding_window.max_consecutive_ones

Max Consecutive Ones

Problem Statement: Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Examples
Input : nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0] , k = 3
Output : 10
Explanation : The maximum number of consecutive 1's are obtained only if we flip the 0's present at position 3, 4, 5 (0 base indexing).
The array after flipping becomes [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0].
The number of consecutive 1's is 10.


Input : nums = [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1] , k = 3
Output : 9
Explanation : The underlines 1's are obtained by flipping 0's in the new array.
[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1].
The number of consecutive 1's is 9.
"""


def max_consecutive_ones(nums: list[int], k: int):
    zeros = 0
    max_len = 0

    left = 0

    # Right pointer iterates through array
    for r in range(len(nums)):
        # If current element is 0, increment zero counter
        if nums[r] == 0:
            zeros += 1

        # If number of zeros > k, shrink window from left
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1

            # Move left pointer forward
            left += 1

        max_len = max(max_len, r - left + 1)
    return max_len


if __name__ == "__main__":
    res = max_consecutive_ones([1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3)
    print(res)
