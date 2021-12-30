"""
loop
array/str value append
recuirse  - adds to output array
pop that value appeneded

"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        cur = []
        
        def helper(nums, cur, output):
            output.append(cur)
            for i,n in enumerate(nums):                
                helper(nums[i+1:], cur + [nums[i]], output)

        helper(nums, cur, output)                
        return output            
                
