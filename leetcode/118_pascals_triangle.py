"""
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
"""

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        result = [[1]]
        for row in range(0, numRows - 1):
            last_row = result[row]
            current_row = [1]
            for i in range(1, len(last_row)):
                current_row.append(last_row[i - 1] + last_row[i])
            current_row.append(1)
            result.append(current_row)

        return result

# Run and Test
s = Solution()
print(s.generate(5))
print(s.generate(3))
print(s.generate(2))
print(s.generate(1))