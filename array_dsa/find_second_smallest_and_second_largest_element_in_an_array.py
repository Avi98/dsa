"""
Docstring for array.find_second_smallest_and_second_largest_element_in_an_array
"""


def find_second_smallest_and_second_largest_element_in_an_array(nums: list[int]):

    largest_x = float("-inf")
    smallest_x = float("inf")

    sec_small = float("inf")
    sec_large = float("-inf")

    for i in nums:
        largest_x = max(i, largest_x)
        smallest_x = min(i, smallest_x)

    for i in nums:
        if i < sec_small and i != smallest_x:
            sec_small = i

        if i > sec_large and i != largest_x:
            largest_x = i

    print(sec_large, sec_small)


if __name__ == "__main__":
    find_second_smallest_and_second_largest_element_in_an_array([2, 2, 4, 7, 7, 5])
