"""
Problem Statement: Given an array of length N, peak element is defined as the element greater than both of its neighbors. Formally, if arr[i] is the peak element, arr[i - 1] < arr[i] and arr[i + 1] < arr[i]. Find the index(0-based) of a peak element in the array.
If there are multiple peak numbers, return the index of any peak number.

Input: arr[] = {1,2,3,4,5,6,7,8,5,1}
Output: 7
Explanation: There is only 1 peak element, 8,  that is at index 7.
Input: arr[] = {1,2,1,3,5,6,4}
Output: 1
Explanation : There are 2 peak numbers that are at indices 1 and 5. We can return any of them.
"""

def peak_element_in_array(arr: list[int]) -> int:
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = (low + high) // 2
        if arr[mid] > arr[mid + 1]:
            high = mid
        else:
            low = mid + 1
    return low


if __name__ == "__main__":
    ans = peak_element_in_array([1, 2, 1, 3, 5, 6, 4])
    print(ans)
