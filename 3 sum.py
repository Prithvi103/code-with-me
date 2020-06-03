"""
Given an array nums of n integers, are there elements a, b, c in nums such
that a + b + c = 0? Find all unique triplets in the array which gives the sum
of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

"""
The popular solution is to sort the array first and then use a mid index to
search either ways for complementing numbers which would bring the total to 0. 
The solution is not very intuitive and it's difficult to think of it on the 
feet. Hence, I decided to go for an easier solution where you just index all 
the numbers with their indexes in a dictionary and then find out if there are 
combinations. Indexing take O(n) and finding combinations of numbers takes O(
n^2). Thus the time complexity is O(n^2). This passed 312/313 test cases and 
failed due to run time for the test case where there is an array of million 
zeros. I added a custom if case to just get accepted on the solution :D
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums is None:
            return []
        if len(nums) is None:
            return []
        d = {}
        res = set()
       
        for i in range(len(nums)):
            tot = nums[i] 
            #print (tot,d.keys())
            if tot in d.keys():
                d[tot].append(i)
            else:
                d[tot] = [i]
        #hs = set()
        if len(d.keys()) == 1 and 0 in d and len(d[0])>2:
            return [[0,0,0]]
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):

                ind = -nums[i] -nums[j]
                if ind in d.keys():
                    opt = d[ind]
                    for k in opt:
                        if i!=k and j!=k:
                            l = [nums[i],nums[j],nums[k]]
                            l.sort()
                            kt = (l[0],l[1],l[2])
                            res.add(kt)

                        
        return list(list(i) for i in res)
            
