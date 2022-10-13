"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}
        for x in nums1:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1

        res = []
        for x in nums2:
            if x in count:
                res.append(x)
                count[x] -= 1
                if count[x] == 0:
                    count.pop(x)

        return res