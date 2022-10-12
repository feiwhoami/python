"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        for x in s:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1

        for x in t:
            if x in count:
                count[x] -= 1
                if count[x] == 0:
                    count.pop(x)
            else:
                return False

        return len(count) == 0

# Run and Test
s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("rat", "car"))

