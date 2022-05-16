"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        end = 0
        first = strs[0]
        while end <= len(first):
            for x in strs:
                if len(x) <= end or x[end] != first[end]:
                    return first[:end] 
            end += 1
        
        return ""

# Run and Test
s = Solution()
print (s.longestCommonPrefix(["flower","flow","flight"]))
print (s.longestCommonPrefix(["dog","racecar","car"]))
print (s.longestCommonPrefix(["ab", "a"]))
print (s.longestCommonPrefix(["a"]))
print (s.longestCommonPrefix([""]))