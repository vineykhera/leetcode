"""

[0,3,1,6,2,2,7].

 1 1 1 1 1 1 1
 1 2 2 3     4
 
10,9,2,5,3,7,101,18
 1 1 1 1 1 1 1   1
 1 1 1 2 2 3  4  4

[0,1,0,3,2,3]
 1 2 2 3 3 4

3,6,2,7

[4,10,4,3,8,9]
 1  2 2 2 3  4


"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        out = [1] * len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j] :
                    out[i] = max(out[i],out[j] + 1)
        return max(out)
        
        