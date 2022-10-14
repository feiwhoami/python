"""
Given the root of a binary tree, return the sum of all left leaves.
A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

Example 2:
Input: root = [1]
Output: 0
"""

from turtle import left
from typing import Optional
from typing import List
from common.tree import TreeNode

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        left_nodes = []
        self._helper(root, False, left_nodes)
        return sum(left_nodes)
    
    def _helper(self, node: TreeNode, is_left: bool, left_nodes: List[int]) -> None:
        if not node.left and not node.right and is_left:
            left_nodes.append(node.val)
            return

        if node.left:
            self._helper(node.left, True, left_nodes)
        if node.right:
            self._helper(node.right, False, left_nodes)

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        else:
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)