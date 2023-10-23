"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                sub1 = s[:left] + s[left + 1:]
                sub2 = s[:right] + s[right + 1:]
                return sub1 == sub1[::-1] or sub2 == sub2[::-1]
            left += 1
            right -= 1

        return True

# Run and Test
s = Solution()
print(s.validPalindrome("temmeb"))