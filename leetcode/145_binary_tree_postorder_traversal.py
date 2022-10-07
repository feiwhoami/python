"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]

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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self._helper(root, res)
        return res


    def _helper(self, node: Optional[TreeNode], res: List[int]) -> None:
        if not node:
            return

        self._helper(node.left, res)
        self._helper(node.right, res)
        res.append(node.val)
