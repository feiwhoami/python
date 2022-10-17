"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2
"""

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        start, end, max_len = 0, 0, 0
        while end < len(nums):
            if not nums[start]:
                start += 1
                end = start
                continue

            if nums[end]:
                max_len = max(max_len, end - start + 1)
                end += 1
            else:
                start = end

        return max_len

# Run and Test
s = Solution()
print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))