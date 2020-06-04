"""
Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.
Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000
Follow up:

Can you solve it using only one pass?
Can you solve it in O(1) space?
"""

"""
Solved by considering situations where the current number is greater, lesser and equal to the 
previous number. Single pass O(n) solution and O(1) time complexity.
"""

class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if A is None or len(A) < 3:
            return 0
        start = False
        down = False
        up = False
        highest = 0
        l = 1
        for i in range(1,len(A)):
            if i==(len(A)-1):
                if up:
                    
                    if A[i]<A[i-1]:
                        l+=1
                        if l>highest:
                            highest = l
            if A[i]>A[i-1]:
                if down and up:
                    if l>highest:
                        highest = l
                    l = 1
                    down = False
                if up is False:
                    up = True
                    start = True
                    l = 1
                l += 1
            if A[i]<A[i-1]:
                if up:
                    down = True
                else:
                    continue
                l+=1
            if A[i] == A[i-1]:
                if up:
                    if down:
                        up = False
                        down = False
                        if l>highest:
                            highest = l
                        l = 1
                        
                    else:
                        up = False
                        l = 1
                else:
                    continue
        return highest