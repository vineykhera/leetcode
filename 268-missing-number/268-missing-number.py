class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        stdset = set(i for i in range(n+1))
        return sum(stdset) - sum(nums)