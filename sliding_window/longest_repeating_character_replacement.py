"""
Docstring for sliding_window.longest_repeating_character_replacement

longest repeating character replacement

Problem Statement: Given an integer k and a string s, any character in the string can be selected and changed to any other uppercase English character.
This operation can be performed up to k times. After completing these steps, return the length of the longest substring that contains the same letter.

Input: s = "BAABAABBBAAA", k = 2
Output: 6
Explanation: We can change the B at index 0 and 3 (0-based indexing) to A. The new string becomes "AAAAAABBBAAA". The substring "AAAAAA" is the longest substring with the same letter, and its length is 6.


Input: s = "AABABBA", k = 1
Output: 4
Explanation: We can change one character to get the new string "AABBBBA". The substring "BBBB" is the longest with the same character. There are other ways to achieve this result as well.
"""


def longest_repeating_character_replacement(s: str, k: int):
    """
    Docstring for longest_repeating_character_replacement
    1. maintin a

    :param s: Description
    :type s: str
    :param k: Description
    :type k: int
    """
    l_index = 0
    map_freq = {}

    curr_max_sub_str = 0
    max_freq = 0

    for r_index, r_char in enumerate(s):
        map_freq[r_char] = map_freq.get(r_char, 0) + 1

        curr_max_sub_str = max(max_freq, map_freq.get(r_char, 0))
        while (r_index - l_index + 1) - max_freq > k:
            map_freq.pop(s[l_index])
            l_index += 1
        curr_max_sub_str = max(curr_max_sub_str, r_index - l_index + 1)


if __name__ == "__main__":
    pass
