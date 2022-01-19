class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(strt, path):
            if sum(path) == target:
                res.append(path[:])
            if sum(path) < target:
                for i in range(strt, len(candidates)):
                    if i > strt and candidates[i-1] == candidates[i]:
                        continue
                    if sum(path)+candidates[i] <= target:
                        backtrack(i+1, path+[candidates[i]])
        
        strt = 0
        candidates.sort()
        backtrack(strt, [])
        return res        