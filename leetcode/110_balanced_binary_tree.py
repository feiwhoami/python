"""
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
"""

from typing import Optional
from common.tree import TreeNode

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self._helper(root) != -1

    
    def _helper(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        
        left = self._helper(node.left)
        if left < 0:
            return -1

        right = self._helper(node.right)
        if right < 0:
            return -1

        if abs(left - right) > 1:
            return -1
        
        return max(left, right) + 1
