"""
edges - 

"""
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        st = []
        def pathexists(x,y):
            st.append(x)
            visited = set()
            # print(x,y)
            # print(x, graph[x])
            graph[x].remove(y)
            # print(x, graph[x])
            
            while st:
                cur = st.pop()
                if cur not in visited:                
                    visited.add(cur)
                    for nei in graph[cur]:
                        if nei not in visited:
                            # visited.add(nei)
                            st.append(nei)
                            if nei == y:
                                return [x,y]
                                        
            
            
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        for i in range(len(edges)-1,-1,-1):
            x,y = edges[i]
            if pathexists(x,y):
                return [x,y]
            
        

        return None