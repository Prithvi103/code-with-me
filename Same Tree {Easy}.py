"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have 
the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
"""
"""
DFS solution which runs in O(n) time.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        a = self.traverse(p,q)
        return not a
        
    def traverse(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return False
        if p is None or q is None:
            return True
        if p.val != q.val:
            return True
        a = (self.traverse(p.left,q.left) or self.traverse(p.right,q.right))
        return a
        