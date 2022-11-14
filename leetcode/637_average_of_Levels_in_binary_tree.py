"""
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.
Answers within 10^-5 of the actual answer will be accepted.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].

Example 2:
Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
"""

from typing import List
from typing import Optional
from common.tree import TreeNode

class Solution:
    def __init__(self):
        self.res = []


    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return self.res

        self._helper([root])
        return self.res


    def _helper(self, curr_level: List[TreeNode]):
        if not curr_level:
            return
        
        avg = sum([n.val for n in curr_level]) / len(curr_level)
        self.res.append(avg)

        next_level = []
        for node in curr_level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        self._helper(next_level)