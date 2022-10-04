"""
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
"""

from typing import Optional
from common.tree import TreeNode

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self._helper(root, 0)


    def _helper(self, node: Optional[TreeNode], curr_depth: int) -> int:
        if node is None:
            return curr_depth
        
        return max(self._helper(node.left, curr_depth), self._helper(node.right, curr_depth)) + 1