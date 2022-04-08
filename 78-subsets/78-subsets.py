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

def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtracking(res,0,[],nums)
        return res
    
    def backtracking(self,res,start,subset,nums):
        res.append(list(subset))
        for i in range(start,len(nums)):
            subset.append(nums[i])
            self.backtracking(res,i+1,subset,nums)
            subset.pop()

"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        out = []
        
        def helper(nums, path, cur):
            # print("path", path)
            if cur == len(nums):
                out.append(path)
                return out
            
            # for i in range(cur, len(nums)):
            helper(nums, path+[nums[cur]],cur+1)
            helper(nums, path, cur+1)
            
            
        helper(nums, [], 0)
        return out
        