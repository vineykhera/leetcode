"""
backtracking or dp

dp start crom back 


"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        L = len(cost)
        # dp = cost.copy()
        # mincost = 0
        # i = L-2
        i = 2
        while i <= L-1:
            cost[i] = min(cost[i-1], cost[i-2]) + cost[i]
            i += 1
          
        return min(cost[L-1], cost[L-2])
            