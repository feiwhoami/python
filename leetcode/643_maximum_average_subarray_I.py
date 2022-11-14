"""
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
Any answer with a calculation error less than 10-5 will be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000
"""

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sub_sum = sum(nums[:k])
        res = sub_sum

        for i in range(k, len(nums)):
            sub_sum += nums[i]
            sub_sum -= nums[i - k]
            if res < sub_sum:
                res = sub_sum

        return res / k

# Run and Test
s = Solution()
print(s.findMaxAverage([0,1,1,3,3], 4))