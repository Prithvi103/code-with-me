"""
Given an array of integers nums sorted in non-decreasing order, find the
starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""

"""
Simple binary search with constant space
"""
class Solution:
    def __init__(self):
        self.left = -1
        self.right = -1
    def inspectRange(self, nums: List[int], cur: int, start: int, end: int, target: int):
        # print (nums, cur, start, end, target)
        if start>end:
            return
        if nums[cur] == target:
            if self.left==-1 or cur<self.left:
                self.left = cur
            if self.right < cur:
                self.right = cur
            start1 = cur + 1
            end1 = cur - 1
            cur = (start + end1)//2
            Solution.inspectRange(self, nums, cur, start, end1, target)
            cur = (start1 + end)//2
            Solution.inspectRange(self, nums, cur, start1, end, target)
        elif nums[cur] < target:
            start = cur + 1
            cur = (start + end)//2
            Solution.inspectRange(self, nums, cur, start, end, target)
        else:
            end = cur - 1
            cur = (start + end)//2
            Solution.inspectRange(self, nums, cur, start, end, target)          
        return
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        if l==0:
            return [-1, -1]
        Solution.inspectRange(self, nums, l//2, 0, l-1, target)
        return [self.left, self.right]