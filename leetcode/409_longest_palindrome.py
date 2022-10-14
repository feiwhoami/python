"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_set = set()
        res = 0
        for c in s:
            if c not in s_set:
                s_set.add(c)
            else:
                res += 2
                s_set.remove(c)

        if len(s_set) != 0:
            res += 1

        return res
