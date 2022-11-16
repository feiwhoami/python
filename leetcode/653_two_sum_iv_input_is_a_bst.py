"""
Given the root of a Binary Search Tree and a target number k,
return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Example 2:
Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
"""

from typing import Optional
from typing import Set
from common.tree import TreeNode

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return self._helper(root, set(), k)

    
    def _helper(self, node: TreeNode, val_set: Set[int], k: int) -> bool:
        if not node:
            return False

        if k - node.val in val_set:
            return True

        val_set.add(node.val)
        return self._helper(node.left, val_set, k) or self._helper(node.right, val_set, k)