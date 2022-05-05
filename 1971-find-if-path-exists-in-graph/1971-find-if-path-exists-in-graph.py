class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        
         1 - 2 -3 - 4
        """
        visited = set()
        que = deque([source])
        
        if n==1 and source == destination:
            return True
        
        dic = defaultdict(list)
        
        for i, j in edges:
            dic[i].append(j)
            dic[j].append(i)
        
#         while que:
#             node = que.popleft()
#             visited.add(node)
#             if node == destination:
#                 return True

#             for n in dic[node]:        
#                 if n not in visited:
#                     que.append(n)
                        
#         return False
                
        stack = [source]
        
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            visited.add(node)
            for n in dic[node]:
                if n not in visited:
                    stack.append(n)
        return False
        