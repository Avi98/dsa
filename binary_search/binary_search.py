"""
Quick sort algo always work in sorted array
[1,2,3,4,5,6,7] target 5

"""

import math


class Solution:
    def __init__(self) -> None:
        pass

    def iterative_binary(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = math.ceil((low + high) / 2)
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def recursive_binary(self, nums: list[int], target: int, low: int, high: int):

        if low >= high:
            return -1
        mid = math.ceil((low + high) / 2)

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            self.recursive_binary(nums=nums, target=target, low=mid + 1, high=high)
        else:
            high = mid - 1
            self.recursive_binary(nums=nums, target=target, low=mid + 1, high=high)


if __name__ == "__main__":
    res = Solution().iterative_binary([1, 2, 3, 4, 5, 6, 7], 6)
    res_recursion = Solution().recursive_binary([1, 2, 3, 4, 5, 6, 7], 6, low=0, high=6)

    print(res)
    print(res_recursion)
