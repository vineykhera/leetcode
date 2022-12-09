class Solution:
    def tribonacci(self, n: int) -> int:
        dic = {}
        def helper(n, dic):
            if n == 0:
                dic[n] = 0
            elif n == 1:
                dic[n] = 1
            elif n == 2:
                dic[n] = 1
            else:
                dic[n] = dic[n-1] + dic[n-2] + dic[n-3]
        for i in range(n+1):
            helper(i, dic)
        return dic[n]        