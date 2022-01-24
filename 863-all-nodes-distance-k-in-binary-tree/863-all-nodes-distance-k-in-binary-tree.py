# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
target
findtargetlevel
start again and 
keep comparing difference with other levels

"""
import collections

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        #error check 
        if not root or not target:
            return []
        if k==0:
            return [target.val]
        
        def converttograph():
            adjList = defaultdict(list)
            q = deque()
            q.append(root)
            while q:
                node = q.popleft()
                if node.left:
                    adjList[node.left].append(node)
                    adjList[node].append(node.left)    
                    q.append(node.left)

                if node.right:
                    adjList[node.right].append(node)
                    adjList[node].append(node.right)   
                    q.append(node.right)
            return adjList
                    
        
        #convert to grapth
        graph = converttograph()
        # print("grapth", graph)
        visited = set()
        level = 0
        dq = deque()
        dq.append((target,level))
        # looplevel = 0
        res = []

        #check levels
        while dq and level <= k:
            node, level  = dq.popleft()
                
            if node not in visited:
                # print("node", level, graph[node])
                if level == k:
                    res.append(node.val)
                for children in graph[node]:
                    dq.append((children,level+1))
                # looplevel += 1
                visited.add(node)
            
                    
        return res
        