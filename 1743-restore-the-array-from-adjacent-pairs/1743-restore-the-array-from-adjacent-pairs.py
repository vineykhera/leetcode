class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        ans = []
        seen = set()
        st = []
        graph = defaultdict(list)
        for x,y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)
            
        for u in graph:
            if len(graph[u]) == 1:
                cur = u
                break
        st = [cur]
        
        while st:
            cur = st.pop()
            seen.add(cur)
            ans.append(cur)
            neig = graph[cur]
            # cur = None
            for n in neig:
                if n not in seen:
                    st.append(n)
            
        return ans
        