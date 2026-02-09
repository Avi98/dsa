"""
 Given an array of integers, find the maximum sum of a subarray with a fixed window size.

Let’s consider the array: [2, 1, 5, 1, 3, 2] and a window size of 3.
"""


def find_avg_of_sum(s: list[int], k: int):
    window_sum = 0
    sum_max = sum(s[:k])

    for i in range(k, len(s)):
        window_sum += s[i] - s[k]

        sum_max = max(sum_max, window_sum)

    return sum_max


if __name__ == "__main__":
    res = find_avg_of_sum([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)
    print(res)
