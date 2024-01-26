class Solution:
    def maxArea(self, h: List[int]) -> int:
        l = 0
        r = len(h) - 1
        res = 0
        while l < r:
            res = max(res, min(h[l], h[r])*(r-l))
            # print(res)
            if h[l] < h[r]:
                l = l+1
            else:
                r = r - 1
        return res
            
        