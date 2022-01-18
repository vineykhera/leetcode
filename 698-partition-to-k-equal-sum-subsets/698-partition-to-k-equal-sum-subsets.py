class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        nums.sort(reverse=True)
        target = sum(nums) // k
        used = [False] * len(nums)
        
        def backtrack(strt, k, pathsum):
            if k == 0:
                return True
            if pathsum == target:
                return backtrack(0,k-1,0)
            
            for i in range(strt, len(nums)):
                if used[i] or pathsum + nums[i] > target:
                    continue
                used[i] = True
                if backtrack(i+1, k, pathsum + nums[i]):
                    return True
                used[i] = False
                
            return False
        return backtrack(0,k,0)