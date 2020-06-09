"""
Given the root of a binary tree, find the maximum value V for which there exists different 
nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an 
ancestor of B.)

Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: 
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
"""

"""
In my solution I maintain a list of all ancestors for every node and iterate to find the 
biggest difference. A more faster solution which is available in the discussions is to just 
maintain a max and min for every subtree and update the maximum difference
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from copy import copy
class Solution:
    def returnDiff(self, root:TreeNode, valDiff:List[int], maxScore:int):
        for i in valDiff:
            tmp = abs(root.val-i)
            if tmp>maxScore:
                maxScore = tmp
        valDiff.append(root.val)
        if root.left is not None:
            leftvalDiff = copy(valDiff)
            leftVal = self.returnDiff(root.left, leftvalDiff, maxScore)
            if (leftVal>maxScore):
                maxScore = leftVal
        if root.right is not None:
            rightvalDiff = copy(valDiff)
            rightVal = self.returnDiff(root.right, rightvalDiff, maxScore)
            if (rightVal>maxScore):
                maxScore = rightVal
        return maxScore
            
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return self.returnDiff(root,[],0)
        
        
        