class Solution:
    def climbstairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dictSteps = {}

        if n == 0:
            numWays = 0
            dictSteps[n] = n
            return numWays
        if n == 1:
            dictSteps[n] = n
            numWays = 1
            return numWays
        if n == 2:
            dictSteps[n] = n
            numWays = 2
            return numWays

        if n-1 in dictSteps and n-2 in dictSteps:
            numWays = dictSteps[n-2] + dictSteps[n-1]
        else:
            dictSteps[n-2] = self.climbstairs(n - 2)
            dictSteps[n-1] = self.climbstairs(n - 1)
            numWays = dictSteps[n - 2] + dictSteps[n - 1]
        return numWays


sol = Solution()
i =2
while i < 37:
    i += 1
    print(i, sol.climbstairs(i))
