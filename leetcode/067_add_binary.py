"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1

        carryon = 0
        result = ""

        while i >= 0 and j>= 0 :
            sum = int(a[i]) + int(b[j]) + carryon
            result = str(sum % 2) + result
            carryon = sum // 2
            i -= 1
            j -= 1

        while i >= 0:
            sum = int(a[i]) + carryon
            result = str(sum % 2) + result
            carryon = sum // 2
            i -= 1

        while j >= 0:
            sum = int(b[j]) + carryon
            result = str(sum%2) + result
            carryon = sum // 2
            j -= 1

        if carryon == 1:
            result = str(1) + result

        return result

    def addBinary2(self, a:str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

# Run and Test
s = Solution()
print(s.addBinary("1010", "1011"))