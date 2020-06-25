"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

"""
A pretty interesting problem. I like coding questions which have a mathematical background to 
it compared to your run of the mill dynamic programming questions. Idea behind is to figure out 
a mathematical formula to find f(n). We know that F(0),F(1) = 1, F(2) = 2, F(3) = 5. Fixing one 
of the numbers as root node we can find that the solution is merely F(0)*F(n-1) + F(1)*F(n-2) 
+.... +F(n-1)*F(0)
"""
class Solution:
    def numTrees(self, n: int) -> int:
        if n is None:
            return None
        arr = [1,1,2,5]
        i = 3
        while i<n:
            i += 1
            result = 0
            for j in range(i//2):
                result += (2*arr[j]*arr[-(j+1)])
            if i%2 == 1:
                k = i//2
                result += (arr[k]*arr[k])
            arr.append(result)
        return arr[n]