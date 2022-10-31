"""
Given the root of a Binary Search Tree (BST),
return the minimum absolute difference between the values of any two different nodes in the tree.

Example 1:
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1
"""

from typing import Optional
from common.tree import TreeNode

class Solution:
    def __init__(self):
        self.min_diff = float('inf')
        self.curr_node = None


    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self._helper(root)
        return self.min_diff


    def _helper(self, node: TreeNode) -> None:
        if not node:
            return
        
        self._helper(node.left)

        if self.curr_node:
            self.min_diff = min(self.min_diff, abs(node.val - self.curr_node.val))
        self.curr_node = node
        
        self._helper(node.right)

# Run and Test
t1 = TreeNode(4)
t2 = TreeNode(2)
t3 = TreeNode(6)
t1.left = t2
t1.right = t3

s = Solution()
print(s.getMinimumDifference(t1))