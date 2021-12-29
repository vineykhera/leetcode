"""
-4, -1,-1, 0, 1,2

counter(nums)
nums[i] + nums[j] + nums[k] == 0

nums[i] + nums[j] == - nums[k] 

0 - 2sum = if that num exist in dic, we foumd a triplet
2sum > sort and loop 

-1: 2

"""
# import collections

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         out = set()
#         dups = set()
#         dic = Counter(nums)
#         for i in range(len(nums)):
#             if nums[i] not in dups:
#                 dups.add(nums[i])
#                 for j in range(i, len(nums)):
#                     if i != j:
#                         twosum = nums[i] + nums[j]
#                         dic[nums[i]] -= 1
#                         dic[nums[j]] -= 1
#                         if dic.get(-twosum,'none') != "none" and dic[-twosum] > 0:
#                             out.add(tuple(sorted((nums[i],nums[j],-twosum))))
#                         dic[nums[i]] += 1
#                         dic[nums[j]] += 1
#         return out
                                
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = set()
        dups = set()
        seen = {}
        for i in range(len(nums)):
            if nums[i] not in dups:
                dups.add(nums[i])
                for j in range(i+1, len(nums)):
                    twosum = nums[i] + nums[j]
                    if seen.get(-twosum,'none') != "none" and seen[-twosum] == i:
                        out.add(tuple(sorted((nums[i],nums[j],-twosum))))
                    seen[nums[j]] = i
        return out