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


def sum_prob(len: int, nums: set[int], target: int):
    """using hashing"""

    hash = {}

    for i in range(len):
        books = list(nums)
        a = books[i]
        more = target - a
        if hash.get(more):
            return "Yes"
        hash[books[i]] = i
        return "No"


if __name__ == "__main__":
    is_yes = sum_prob(5, {2, 6, 5, 8, 11}, 14)

    print(is_yes)
