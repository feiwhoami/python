"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]
"""

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        curr = [1]

        for _ in range (0, rowIndex):
            next = [1]
            for i in range (1, len(curr)):
                next.append(curr[i - 1] + curr[i])
            
            next.append(1)
            curr = next

        return curr

# Run and Test
s = Solution()
print(s.getRow(0))
print(s.getRow(1))
print(s.getRow(2))
print(s.getRow(3))
print(s.getRow(5))
