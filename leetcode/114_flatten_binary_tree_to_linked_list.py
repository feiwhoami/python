"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree. 

Example 1:

Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]
"""

from typing import Optional
from common.tree import TreeNode, print_tree

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root == None:
            return

        pre = None
        stack = [root]

        while (len(stack) != 0):
            cur = stack.pop()
            
            if cur.right != None:
                stack.append(cur.right)

            if cur.left != None:
                stack.append(cur.left)

            if pre != None:
                pre.left = None
                pre.right = cur

            pre = cur
        
        return

# Run and Test
n2 = TreeNode(2)
n3 = TreeNode(3)
n1 = TreeNode(1, n2, n3)

s = Solution()
s.flatten(n1)
print_tree(n1)