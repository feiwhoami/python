"""
Given an integer num, return a string of its base 7 representation.

Example 1:
Input: num = 100
Output: "202"

Example 2:
Input: num = -7
Output: "-10"
"""

class Solution:
    def convertToBase7(self, num: int) -> str:
        res = ""
        negative = False
        if num < 0:
            num = -num
            negative = True
        
        while num >= 7:
            mod = num % 7
            res = str(mod) + res
            num //= 7
        res = str(num) + res

        if negative:
            res = "-" + res

        return res

# Run and Test
s = Solution()
print(s.convertToBase7(7))