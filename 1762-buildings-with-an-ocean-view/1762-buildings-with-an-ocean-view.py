"""
9:44

start from end
keep adding until its increasing, we can add just indexes


"""

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        lastmax = float('-inf')
        res = []
        for i in range(len(heights)-1, -1, -1):            
            if heights[i] > lastmax:
                lastmax = heights[i]
                res.append(i)
        return res[::-1]
                