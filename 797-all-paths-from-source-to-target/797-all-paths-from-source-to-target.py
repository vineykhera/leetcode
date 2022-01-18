"""
0- 1,2
1- 3
2-3
3-

0 to 3
  def allPathsSourceTarget(self, graph):
        def dfs(cur, path):
            if cur == len(graph) - 1: res.append(path)
            else:
                for i in graph[cur]: dfs(i, path + [i])
        res = []
        dfs(0, [0])
        return res


"""

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph)
        
        def backtrack(strt, path):
            if strt == len(graph)-1:
                res.append(path[:])
            else:    
            # for i in range(strt, n):
                for j in graph[strt]:
                    backtrack(j, path+[j])
        
        backtrack(0,[0])
        return res    