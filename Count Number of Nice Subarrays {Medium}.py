"""
Given an array of integers nums and an integer k. A subarray is called nice if there are k odd 
numbers on it.

Return the number of nice sub-arrays.

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
"""

"""
The idea is to find the indices of all odd numbers and find how many numbers are available on 
the left and right of the set of k odd numbers and add (1 + left + right + left*right) for 
every set. Runs in O(n) time and takes O(n) space.
"""

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if nums is None or k is None:
            return 0
        ls = [-1]
        for i in range(n):
            if nums[i]%2==1:
                ls.append(i)
        ls.append(n)
        l= len(ls)
        result = 0
        for i in range(1,l-1):
            if i+k>=l:
                break
           
            end = ls[i+k] - 1
            right = end-ls[i+k-1]
            start = ls[i-1] + 1
            left = ls[i] - start
            #print (start,end,left,right)
            result += (1 + left + right + left*right)
        return result
                
        