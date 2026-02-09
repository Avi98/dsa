"""
Docstring for sliding_window.number_of_sub_arrays_of_size_k

1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

Example 1:

Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
Example 2:

Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.


Constraints:

1 <= arr.length <= 105
1 <= arr[i] <= 104
1 <= k <= arr.length
0 <= threshold <= 104
"""

# todo:
# Avoid Division - Use Integer Comparison (Lines 33, 38)
# Instead of dividing on every iteration:
# if window_sum >= threshold * k:  # More efficient, no float ops
# Why: Integer comparison is faster and avoids floating-point precision issues.


def number_of_sub_arrays_of_size_k(arr: list[int], k: int, threshold: int):
    count = 0
    window_sum = sum(arr[:k])

    if (window_sum / k) >= threshold:
        count += 1

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        if (window_sum / k) >= threshold:
            count += 1

    return count


if __name__ == "__main__":
    res = number_of_sub_arrays_of_size_k(
        arr=[11, 13, 17, 23, 29, 31, 7, 5, 2, 3], k=3, threshold=5
    )
    print(res)
