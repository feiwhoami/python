"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, return the Hamming distance between them.

Example 1:
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.

Example 2:
Input: x = 3, y = 1
Output: 1
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if x == y:
            return 0

        res = 0
        while x != 0 or y != 0:
            if x & 1 != y & 1:
                res += 1
            x >>= 1
            y >>= 1

        return res