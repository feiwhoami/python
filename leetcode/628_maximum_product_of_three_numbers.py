"""
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example 1:
Input: nums = [1,2,3]
Output: 6

Example 2:
Input: nums = [1,2,3,4]
Output: 24

Example 3:
Input: nums = [-1,-2,-3]
Output: -6
"""

from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            res = 1
            for num in nums:
                res *= num 
            return res

        nums = sorted(nums, reverse = True)
        candidate1 = nums[0] * nums[1] * nums[2]
        candidate2 = nums[0] * nums[len(nums) - 2] * nums[len(nums) - 1]

        return max(candidate1, candidate2)