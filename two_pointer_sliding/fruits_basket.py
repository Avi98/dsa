"""
Docstring for two_pointer_sliding.fruits_basket

https://takeuforward.org/data-structure/fruit-into-baskets

Problem Statement: There is only one row of fruit trees on the farm, oriented left to right. An integer array called fruits represents the trees, where fruits[i] denotes the kind of fruit produced by the ith tree.
The goal is to gather as much fruit as possible, adhering to the owner's stringent rules :

There are two baskets available, and each basket can only contain one kind of fruit. The quantity of fruit each basket can contain is unlimited.
Start at any tree, but as you proceed to the right, select exactly one fruit from each tree, including the starting tree. One of the baskets must hold the harvested fruits.
Once reaching a tree with fruit that cannot fit into any basket, stop.
Input :fruits = [1, 2, 1]
Output :3
Explanation : We will start from first tree.
The first tree produces the fruit of kind '1' and we will put that in the first basket.
The second tree produces the fruit of kind '2' and we will put that in the second basket.
The third tree produces the fruit of kind '1' and we have first basket that is already holding fruit of kind '1'. So we will put it in first basket.
Hence we were able to collect total of 3 fruits.


Input : fruits = [1, 2, 3, 2, 2]
Output : 4
Explanation : we will start from second tree.
The first basket contains fruits from second , fourth and fifth.
The second basket will contain fruit from third tree.
Hence we collected total of 4 fruits.
"""


def fruits_basket(num: list[int]) -> int:
    """
    Docstring for fruits_basket
        1. create a dict of number of ele present
        2. left, right pointer
        3. right iterate over the list, update the dict with key -> num[i] : freq,
        4. if len(dict.keys()) > 2
        5.   num[i]: freq - 1
        6. left + 1
    :param num: Description
    :type num: list[int]
    :return: max_fruits: int
    :rtype: int
    """
    basket: dict[int, int] = {}

    left = 0
    max_fruites = 0

    for right in range(len(num)):
        basket[num[right]] = basket.get(num[right], 0) + 1

        while len(basket.items()) > 2:
            basket[num[left]] -= 1
            if basket[num[left]] == 0:
                basket.pop(num[left])
            left += 1
        max_fruites = max(max_fruites, right - left + 1)
    return max_fruites


if __name__ == "__main__":
    res = fruits_basket(num=[1, 2, 3, 2, 2])
    print(res)
