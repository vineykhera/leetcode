class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i, j = 0, 0
        ans = float("-inf")
        nsum = [0] * len(nums)
        # nsum.append(0)
        while j <= len(nums) - 1:
            
            if j >= 1:
                nsum[j] = nsum[j-1] + nums[j]
            else:
                nsum[j] = nums[j]
                
            if j - i == k-1:
                if i > 0:
                    nsum[j] = nsum[j] - nums[i-1]
                # print(nsum[j],ans)
                # print(nsum)
                ans = max(nsum[j],ans)
                # print(ans)
                i += 1
            j += 1
                # ans = ans//k
        return ans/k