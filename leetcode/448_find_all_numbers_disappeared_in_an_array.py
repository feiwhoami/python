"""
Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:
Input: nums = [1,1]
Output: [2]
"""

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        res = []
        for i in range(len(nums)):
            if i + 1 not in nums_set:
                res.append(i + 1)

        return res

# Run and test
s = Solution()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
        