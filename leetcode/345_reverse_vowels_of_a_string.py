"""
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        idx = []
        for i, c in enumerate(s):
            if c in vowels:
                idx.append(i)
        start, end = 0, len(idx) - 1
        while start < end:
            s[idx[start]], s[idx[end]] = s[idx[end]], s[idx[start]]
            start += 1
            end -= 1

        return "".join(s)

# Run and Test
s = Solution()
print(s.reverseVowels("leetcode"))