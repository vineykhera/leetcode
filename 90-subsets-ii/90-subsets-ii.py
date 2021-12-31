class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         out = []
#         cur = []
        
#         def backtracksol(nums, cur = [], out = []):
#             out.apppend(cur)
#             for i in range(len(nums)-1):
#                 backtracksol(nums[i+1:], cur + [nums[i]], out)
             
#         backtracksol(nums, cur, out)
        
#         return out

        out = []
        cur = []
        
        def helper(nums, cur = [], out = []):
            out.append(cur)
            for i, n in enumerate(nums):
                if i > 0 and nums[i-1] == nums[i]:
                    continue
                helper(nums[i+1:], cur + [n], out)
        
        helper(sorted(nums), cur, out)
            
        return out