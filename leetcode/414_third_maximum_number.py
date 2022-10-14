"""
Given an integer array nums, return the third distinct maximum number in this array.
If the third maximum does not exist, return the maximum number.

Example 1:
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.

Example 2:
Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
"""

from typing import List
from queue import PriorityQueue

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_set = set(nums)
        q = PriorityQueue()
        for i in nums_set:
            q.put(i * -1)
        
        if q.qsize() <= 2:
            return q.get() * -1

        q.get()
        q.get()

        return q.get() * -1

# Run and Test
s = Solution()
print(s.thirdMax([1,2]))
