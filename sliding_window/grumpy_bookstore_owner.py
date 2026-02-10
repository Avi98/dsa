"""
Docstring for sliding_window.grumpy_bookstore_owner

Grumpy Bookstore Owner

There is a bookstore owner that has a store open for n minutes. You are given an integer array customers of length n where customers[i] is the number of the customers that enter the store at the start of the ith minute and all those customers leave after the end of that minute.

During certain minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

When the bookstore owner is grumpy, the customers entering during that minute are not satisfied. Otherwise, they are satisfied.

The bookstore owner knows a secret technique to remain not grumpy for minutes consecutive minutes, but this technique can only be used once.

Return the maximum number of customers that can be satisfied throughout the day.

Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3

Output: 16

Explanation:

The bookstore owner keeps themselves not grumpy for the last 3 minutes.

The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.

Example 2:

Input: customers = [1], grumpy = [0], minutes = 1

Output: 1

Constraints:
n == customers.length == grumpy.length
1 <= minutes <= n <= 2 * 104
0 <= customers[i] <= 1000
grumpy[i] is either 0 or 1.

"""


def grumpy_bookstore_owner(customer: list[int], grumpy: list[int], min: int):
    ans = 0

    for i in range(len(grumpy)):
        if grumpy[i] == 0:
            ans += customer[i]

    unsatisfied_customer = 0

    for i in range(min):
        if grumpy[i] == 1:
            unsatisfied_customer += customer[i]
    additional_customer = unsatisfied_customer

    for i in range(min, len(grumpy)):
        if grumpy[i] == 1:
            unsatisfied_customer += customer[i]

        if grumpy[i - min] == 1:
            unsatisfied_customer -= customer[i - min]
        additional_customer = max(unsatisfied_customer, additional_customer)

    return additional_customer + ans


if __name__ == "__main__":
    res = grumpy_bookstore_owner(
        customer=[1, 0, 1, 2, 1, 1, 7, 5], grumpy=[0, 1, 0, 1, 0, 1, 0, 1], min=3
    )
    print(res)
