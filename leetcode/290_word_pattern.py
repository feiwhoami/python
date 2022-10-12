"""
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words) or len(set(pattern)) != len(set(words)):
            return False
        
        match = {}
        for idx, c in enumerate(pattern):
            if c not in match:
                match[c] = words[idx]
            else:
                if match[c] != words[idx]:
                    return False

        return True