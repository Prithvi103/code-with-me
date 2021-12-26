"""
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all
nodes in the last level are as far left as possible. It can have between 1 and 2h nodes
inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""

"""
I have just written a simple solution where I have counted all the nodes of a BST using DP DFS.
So the time complexity is O(n) and the space complexity is O(1). You can make this solution
better by doing early stopping.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    def returnCount (self, base: TreeNode) -> int:
        if base.right is not None:
            return self.returnCount(base.right) + self.returnCount(base.left) + 1
        else:
            if base.left is None:
                return 1
            else:
                return 2
    def countNodes(self, root: TreeNode) -> int:
        if root is not None:
            return self.returnCount(root)
        return 0