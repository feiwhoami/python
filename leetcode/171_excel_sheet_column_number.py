"""
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.
For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Example 1:
Input: columnTitle = "A"
Output: 1

Example 2:
Input: columnTitle = "AB"
Output: 28

Example 3:
Input: columnTitle = "ZY"
Output: 701
"""

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        reverse_title = columnTitle[::-1]

        for i in range(0, len(reverse_title)):
            num = ord(reverse_title[i]) - ord('A') + 1
            res += num * (26 ** i)

        return res

# Run and Test
s = Solution()
print(s.titleToNumber("A"))
print(s.titleToNumber("AB"))
print(s.titleToNumber("ZY"))