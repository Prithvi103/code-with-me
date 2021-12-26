"""
Given an array of non-negative integers nums, you are initially 
positioned at the first index of the array.

Each element in the array represents your maximum jump length at that 
position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. 
Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
"""

"""
I've explored every node starting from the first one to see what's the
fewest jumps required to get from index i to end and saved it in memo.
this way we traverse the list only once. Hence run time is linear O(n)
and storage is also O(n)
"""

class Solution:
    def __init__(self):
        self.Memo = dict()
    def calcJump(self, nums: List[int], cur, jumps) -> int:
        if cur not in self.Memo:
            if cur == len(nums) - 1:
                return jumps
            elif cur >= len(nums) or nums[cur]==0:
                return float(inf)
            candidates = []
            for i in range(1, nums[cur] + 1):
                candidates.append(Solution.calcJump
                	(self, nums, cur + i, jumps + 1))
            result = min(candidates)
            self.Memo[cur] = result - jumps
            return result
        else:
            return self.Memo[cur] + jumps
        
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        return Solution.calcJump(self, nums,0,0)