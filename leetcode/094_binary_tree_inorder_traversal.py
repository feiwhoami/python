"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]
"""

from optparse import Option
from typing import Optional
from typing import List
from common.tree import TreeNode

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return
        result = []

        self._helper(root, result)
        return result
        
    def _helper(self, root: Optional[TreeNode], result: List[int]):
        if root is None:
            return
        
        self._helper(root.left, result)
        result.append(root.val)
        self._helper(root.right, result)
