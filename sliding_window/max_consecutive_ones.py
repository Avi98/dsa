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
    count = sum(nums[:k])
    max_count = max(count, sum(nums))

    for i in range(k, len(nums)):
        if nums[i] == 0:
            count += 1
        else:
            count -= 1
        max_count = max(count, max_count)

    return max_count


if __name__ == "__main__":
    res = max_consecutive_ones([1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3)
    print(res)
