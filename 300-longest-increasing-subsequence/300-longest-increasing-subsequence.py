"""
0 1  0 3 2 3
  
1 0  0 2 2 3
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        # print(dp)
        return max(dp)
                
            
        