"""
Given the root of a binary search tree (BST) with duplicates, return all the mode(s)
(i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.
Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [1,null,2,2]
Output: [2]

Example 2:
Input: root = [0]
Output: [0]
"""

from typing import Optional
from typing import List
from common.tree import TreeNode

class Solution:
    def __init__(self):
        self.prev = None
        self.count = 0
        self.max_count = 0
        self.result = []

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self._helper(root)
        return self.result

    def _helper(self, node: Optional[TreeNode]):
        if not node:
            return

        self._helper(node.left)
        
        self.count = 1 if node.val != self.prev else self.count + 1

        if self.count == self.max_count:
            self.result.append(node.val)
        elif self.count > self.max_count:
            self.result = [node.val]
            self.max_count = self.count

        self.prev = node.val
        self._helper(node.right)

# Run and Test
s = Solution()
t1 = TreeNode(1)
t2 = TreeNode(2)
t1.right = t2
print(s.findMode(t1))