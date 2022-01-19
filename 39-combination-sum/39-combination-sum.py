"""
stop if exceed target
reuse number > 0
= target return


                 2,3,6,7
        2       3        6       7
        



"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(strt, path):
            if sum(path) == target:
                res.append(path[:])
                # strt += 1
            if sum(path) < target:
                for i in range(strt, len(candidates)):
                    if sum(path)+candidates[i] <= target:
                        backtrack(i, path+[candidates[i]])
        
        strt = 0
        # candidates.sort()    
        backtrack(strt, [])
        return res