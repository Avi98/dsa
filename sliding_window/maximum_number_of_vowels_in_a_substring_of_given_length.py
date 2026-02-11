"""
Docstring for sliding_window.maximum_number_of_vowels_in_a_substring_of_given_length

Maximum Number of Vowels in a Substring of Given Length
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

"""


def maximum_number_of_vowels_in_a_substring_of_given_length(string: str, k: int):
    vowels = {"a", "e", "i", "o", "u"}
    count = sum(1 for i in string[:k] if i in vowels)

    max_count = count
    for i in range(k, len(string)):
        if string[i - k] in vowels:
            count -= 1
        if string[i] in vowels:
            count += 1
        max_count = max(count, max_count)

    return max_count


if __name__ == "__main__":
    p = maximum_number_of_vowels_in_a_substring_of_given_length("abciiidef", 3)
    print(p)
