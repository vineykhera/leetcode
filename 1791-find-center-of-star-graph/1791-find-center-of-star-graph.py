class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        dic = defaultdict(list)
        
        for i, j in edges:
            dic[i].append(j)
            dic[j].append(i)
        
        l = len(dic)
        
        for k in dic.keys():
            if len(dic[k]) == l-1:
                return k
            
        
        