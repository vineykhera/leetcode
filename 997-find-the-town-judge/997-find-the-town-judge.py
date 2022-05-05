class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        dic = defaultdict(list)
        invdic = defaultdict(list)
        
        for i, j in trust:
            dic[i].append(j)
            invdic[j].append(i)
        
        l = n - 1
        
        for i in range(1,n+1):
            if len(dic[i]) == 0 and len(invdic[i]) == l:
                return i        
        return -1