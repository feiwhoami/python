"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h_set = set()
        for idx in range (len(nums)):
            if len(h_set) > k:
                h_set.remove(nums[idx - k - 1])
            
            if nums[idx] in h_set:
                return True
            else:
                h_set.add(nums[idx])

        return False

# Run and Test
s = Solution()
print(s.containsNearbyDuplicate([1,2,3,1], 3))
print(s.containsNearbyDuplicate([1,0,1,1], 1))
print(s.containsNearbyDuplicate([1,2,3,1,2,3], 2))