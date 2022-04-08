"""
       []
   [1]      []
 [1,2] [1]    []

cur
helper(cur, nums)
base conditon
set(outarr size) = 2 ^ n 

for loop 
choice
recurse helper ( curr+1)
undo my choice



"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []

        def helper(nums, path, cur, out):
            if cur == len(nums):
                out.append(path)
                return 
            
            # for i in range(cur, len(nums)):
            helper(nums, path+[nums[cur]],cur+1, out)
            helper(nums, path, cur+1, out)
            
            
        helper(nums, [], 0, out)
        return out
        