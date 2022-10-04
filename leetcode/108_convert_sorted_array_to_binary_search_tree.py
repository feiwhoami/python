"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
"""

from typing import List
from typing import Optional
from common.tree import TreeNode

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
 
        return self._helper(nums, 0, len(nums) - 1)
 

    def _helper(self, nums: List[int], start: int, end: int) -> Optional[TreeNode]:
        if start > end:
            return None

        mid = (start + end) // 2
        root = TreeNode(nums[mid])

        root.left = self._helper(nums, start, mid - 1)
        root.right = self._helper(nums, mid + 1, end)

        return root
