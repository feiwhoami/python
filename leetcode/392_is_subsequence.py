"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        idx_s = 0
        idx_t = 0

        while (idx_t < len(t)):
            if s[idx_s] == t[idx_t]:
                idx_s += 1
            idx_t += 1
            
            if idx_s == len(s):
                return True

        return False

# Run and Test
s = Solution()
print (s.isSubsequence("abc", "ahbgdc"))
