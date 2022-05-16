"""
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.
 
Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """ Reverse string method
        x = str(x)
        return x == x[::-1]
        """
        
        if x < 0:
            return False
        
        divider = 1
        while math.floor(x / divider) >= 10:
            divider *= 10

        while x != 0:
            if math.floor(x / divider) != x % 10:
                return False
            
            x = math.floor(x % divider / 10)
            divider = math.floor(divider / 100)

        return True

# Run and Test
s = Solution()
print(s.isPalindrome(1000021))