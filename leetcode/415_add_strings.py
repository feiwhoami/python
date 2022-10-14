"""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

Example 1:
Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:
Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:
Input: num1 = "0", num2 = "0"
Output: "0"
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = num1[::-1], num2[::-1]
        carryon, longest_len = 0, max(len(num1), len(num2))

        res = []
        for i in range(longest_len):
            sum = carryon
            if i < len(num1):
                sum += int(num1[i])
            if i < len(num2):
                sum += int(num2[i])
            res.append(sum % 10)
            carryon = sum // 10
        if carryon != 0:
            res.append(carryon)

        return "".join(str(i) for i in res[::-1])
