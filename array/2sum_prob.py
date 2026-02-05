"""
# Problem Statement: Given an array of integers arr[] and an integer target.

# 1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.

# 2nd variant: Return indices of the two numbers such that their sum is equal to the target.
# Otherwise, we will return {-1, -1}.


Input: N = 5, arr[] = {2,6,5,8,11}, target = 14
Output : YES
Explanation: arr[1] + arr[3] = 14. So, the answer is “YES” for first variant for second variant output will be : [1,3].

Input: N = 5, arr[] = {2,6,5,8,11}, target = 15
Output : NO.
Explanation: There exist no such two numbers whose sum is equal to the target.

"""


def two_sum(nums: list[int], target: int) -> bool:
    """Check if two numbers sum to target using hashing.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    seen: set[int] = set()

    for num in nums:
        if target - num in seen:
            return True
        seen.add(num)

    return False


if __name__ == "__main__":
    result = two_sum([2, 6, 5, 8, 11], 14)
    print("YES" if result else "NO")
