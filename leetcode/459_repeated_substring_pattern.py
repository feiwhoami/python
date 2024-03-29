"""
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false

Example 3:
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        sub_str_len = 1

        while sub_str_len <= len(s) // 2:
            if len(s) % sub_str_len == 0:
                s_split = [s[i : i + sub_str_len] for i in range(0, len(s), sub_str_len)]
                if len(set(s_split)) == 1:
                    return True
            sub_str_len += 1

        return False

# Run and Test
s = Solution()
print(s.repeatedSubstringPattern("abab"))