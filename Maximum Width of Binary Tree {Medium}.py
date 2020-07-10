"""
Given a binary tree, write a function to get the maximum width of the given tree. The width of 
a tree is the maximum width among all levels. The binary tree has the same structure as a full 
binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right 
most non-null nodes in the level, where the null nodes between the end-nodes are also counted 
into the length calculation.

Example 1:

Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:

Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
"""

"""
It looks like a tricky problem at first but it's intuitive that a DFS solution should work. I 
calculated the indices at every level using DFS and calculated the maximum width by taking the 
max of difference between the highest and lowest index of every level. Run time is O(n) for 
traversing every node.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        d = defaultdict(list)
        h = 0
        self.traverse(root,d,1,1)
        l = []
        for key in d.keys():
            l.append(d[key][-1]-d[key][0]+1)
        return max(l)
        
    def traverse(self, cur, d, h, val):
        d[h].append(val)
        #print(h,val)
        if cur.left is not None:
            self.traverse(cur.left,d,h+1,val*2-1)
        if cur.right is not None:
            self.traverse(cur.right,d,h+1,val*2)
        return
        
