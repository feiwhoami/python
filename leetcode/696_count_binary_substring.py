"""
Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's,
and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's:
"0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

Example 2:
Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
"""

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # Initialize variables
        pre_len = 0
        cur_len = 1
        count = 0
        
        # Traverse through the string
        for i in range(1, len(s)):
            # If the current character is the same as the previous character
            if s[i] == s[i-1]:
                cur_len += 1
            # If the current character is different from the previous character
            else:
                pre_len = cur_len
                cur_len = 1
                
            # If the previous length is greater than or equal to the current length
            # then we have a valid substring
            if pre_len >= cur_len:
                count += 1
        
        # Return the total count of valid substrings
        return count


# Run and Test
s = Solution()
print(s.countBinarySubstrings("00110011"))