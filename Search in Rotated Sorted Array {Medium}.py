"""
here is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
"""

"""
Find pivot first using binary search and then apply BST on sublist or 
whole list if not rotated
"""
class Solution:
    def findPivot(self, nums:List[int], cur:int, start:int, end:int) -> int:
        if start > end:
            return -1
        if cur != len(nums) - 1 and nums[cur] > nums[cur + 1]:
            return cur
        start1 = cur + 1
        end1 = cur - 1
        cur1 = (start1 + end) // 2
        cur2 = (start + end1) // 2
        return max(Solution.findPivot(self, nums, cur1, start1, end), Solution.findPivot(self,nums,cur2, start,end1))
    
    def BST(self, nums:List[int], cur:int, start:int, end:int, target:int) -> int:
        if start > end:
            return -1
        if nums[cur] == target:
            return cur
        elif nums[cur] < target:
            return Solution.BST(self, nums, ((cur + 1 + end)//2), cur+1, end, target)
        else:
            return Solution.BST(self, nums, ((cur - 1 + start)//2), start, cur - 1, target)
        
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        if len(nums) == 0:
            return -1
        pivot = Solution.findPivot(self,nums,(l//2),0,l-1)
        if pivot==-1:
            return Solution.BST(self,nums,(l//2), 0, l-1,target)
        elif nums[0] == target:
            return 0
        elif(nums[0] < target):
            return Solution.BST(self,nums,(pivot//2), 0, pivot,target)
        else:
            return Solution.BST(self,nums,((pivot + l)//2), pivot + 1, l-1,target)
        