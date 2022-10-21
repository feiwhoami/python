"""
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:
the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

Example 1:
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]

Example 2:
Input: words = ["omk"]
Output: []

Example 3:
Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]
"""

from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_set = set("qwertyuiop")
        second_set = set("asdfghjkl")
        third_set = set("zxcvbnm")
        res = []

        for word in words:
            if set(word.lower()).issubset(first_set) \
                or set(word.lower()).issubset(second_set) \
                or set(word.lower()).issubset(third_set):
                res.append(word)

        return res
