"""
Search Single Element in a sorted array

Problem Statement: Given an array of N integers. Every number in the array except one appears twice. Find the single number in the array.

Input : arr[] = {1,1,2,2,3,3,4,5,5,6,6}
Output: 4
Explanation: Only the number 4 appears once in the array.

Input: arr[] = {1,1,3,5,5}
Output : 3
Explanation: Only the number 3 appears once in the array.

"""


import math

def search_single_elem(arr:list[int]) -> int:
    low = 0
    high = len(arr) - 1

    # todo: handle edge case like if arr is of len 1
    # last ele is unique if arr[n - 1] != arr[n - 2]:   return arr[n - 1]
    
    while low < high:
        mid = math.ceil((low + high)/2)
        # check mid ele
        if arr[mid] != arr[mid + 1] and arr[mid] != arr[mid -1]:
            return mid
        if (mid % 2 == 1 and arr[mid] == arr[mid - 1]) or \
               (mid % 2 == 0 and arr[mid] == arr[mid + 1]):
                # Move to the right half
                low = mid + 1
        else:
                # Move to the left half
                high = mid - 1
    return -1
        

if __name__ == "__name__":
    