"""
Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A 
grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.

 

Example 1:
					6
			7					8
	2			7			1			3
9			1		4						5


Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are 
the even-value grandparents.
"""
"""
Classic DFS problem works in O(N) time and O(1) space
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        result = 0
        result += self.traverse(root, None, None, 0)
        return result
    def traverse(self,cur, par,grap,total):
        if grap is not None and grap.val%2==0:
            total+=cur.val
        if cur.left is not None:
            total = self.traverse(cur.left,cur,par,total)
        if cur.right is not None:
            total = self.traverse(cur.right,cur,par,total)
        return total