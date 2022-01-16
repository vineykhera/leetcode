class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
   
        result = list()
        
        # base case -- least valid input
        if len(nums) == 1:
            return [nums]
        
        for idx in range(len(nums)):
            
            # compute the permutation for ith element
            current_nums = nums[:idx] + nums[idx+1:]
            
            # recursive case
            perms = self.permute(current_nums)

            # permutation generated above don't have the 
            # ith element, so append it
            for perm in perms:
                perm.append(nums[idx])
                
            
            # update the overall results with all (multiple) permutations
            result.extend(perms)
            
        #return all permutations
        return result    


#     def permute(self, nums: List[int]) -> List[List[int]]:
#         result = []
        
#         if (len(nums) == 1):
#             return [nums[:]]
        
#         for _ in range(len(nums)):
#             n = nums.pop(0)
#             perms = self.permute(nums)
       
#             for perm in perms:
#                 perm.append(n) # [2,3]+[1] and [3,2]+[1] individually
#             result.extend(perms) # [2,3,1],[3,2,1] all together into the result
#             nums.append(n)
#         return result
 

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         result = []
#         n = len(nums)
#         def backtrack(perm):
#             if len(perm) == len(nums):
#                 result.append(perm.copy())
#                 return
#             for i in range(n):
#                 if nums[i] in perm:
#                     continue
#                 perm.append(nums[i])
#                 backtrack(perm)
#                 perm.pop()
#         backtrack([])
#         return result


