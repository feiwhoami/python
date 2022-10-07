"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]
"""

from typing import Optional
from typing import List
from common.tree import TreeNode

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self._helper(root, res)
        return res
    

    def _helper(self, node: Optional[TreeNode], res: List[int]) -> None:
        if not node:
            return
        
        res.append(node.val)
        self._helper(node.left, res)
        self._helper(node.right, res)
