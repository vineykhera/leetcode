"""




"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backtrack(i,path, result):
            # print(path)
            if len(path) == k:
                result.append(path[:])
                # print("result", result)
                # return
            
            for j in range(i,n+1):
                path.append(j)
                backtrack(j+1,path,result)
                path.pop()
                
        backtrack(1,[], result)
        # print("print result", result)
        
        return result