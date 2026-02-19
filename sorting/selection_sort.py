"""
Docstring for sorting.selection_sort

Given an array of N integers, write a program to implement the Selection sorting algorithm.

Example 1:
Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: After sorting the array is: 9, 13, 20, 24, 46, 52

Example 2:
Input: N=5, array[] = {5,4,3,2,1}
Output: 1,2,3,4,5
Explanation: After sorting the array is: 1, 2, 3, 4, 5


"""

T = list | set


class Solution:
    def selection_sort(self, number: T, length: int) -> T:

        num = list(number)
        for i in range(0, length - 1):
            min_index = i

            for j in range(i, length):
                if num[j] < num[min_index]:
                    min_index = j

            num[i], num[min_index] = num[min_index], num[i]

        return num


if __name__ == "__main__":
    merge_sort = Solution().selection_sort({13, 46, 24, 52, 20, 9}, 6)
    print(merge_sort)
