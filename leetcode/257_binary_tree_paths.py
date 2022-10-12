"""
Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children.

Example 1:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Example 2:
Input: root = [1]
Output: ["1"]
"""

from typing import Optional
from typing import List
from common.tree import TreeNode

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        res = []
        self._helper(root, "", res)

        return res

    def _helper(self, node: TreeNode, curr_path: str, res: List[str]) -> None:
        if curr_path:
            curr_path += "->"
        curr_path += str(node.val)

        if not node.left and not node.right:
            res.append(curr_path)
            return

        if node.left:
            self._helper(node.left, curr_path, res)

        if node.right:
            self._helper(node.right, curr_path, res)
