import math
import itertools
from itertools import combinations


def getScore_wrong(s):
    return max_Pal_Subsequence(s, 0, len(s)-1)


def max_Pal_Subsequence(s, start, end):

    if start > end:
        return 0
    if start == end:
        return 1
    if s[start] == s[end]:
        return max_Pal_Subsequence(s, start + 1, end - 1) + 2

    incstart = max_Pal_Subsequence(s, start + 1, end)
    decend = max_Pal_Subsequence(s, start, end - 1)
    if incstart > decend:
        return incstart
    else:
        return decend


def getScore(s):
  length = len(s)
  lps_dp = [[0 for i in range(length)] for j in range(length)]

  for i in range(length):
    lps_dp[i][i] = 1

  for i in range(1, length):
    for j in range(i-1, -1, -1):
        if s[i] == s[j]:
            lps_dp[i][j] = lps_dp[i-1][j+1] + 2
        else:
            lps_dp[i][j] = max(lps_dp[i - 1][j], lps_dp[i][j + 1])

  res = 0

  for i in range(length-1):
    res = max(res, lps_dp[i][0] * lps_dp[-1][i+1])

  return res


def getScore2(s):
    n = len(s)
    LPS = [[0] * n for i in range(n)]
    for i in range(n):
        LPS[i][i] = 1
    for le in range(2, n + 1):
        for i in range(n - le + 1):
            j = i + le - 1
            if le == 2 and s[i] == s[j]:
                LPS[i][j] = 2
            elif s[i] == s[j]:
                LPS[i][j] = 2 + LPS[i + 1][j - 1]
            else:
                LPS[i][j] = max(LPS[i + 1][j], LPS[i][j - 1])
    ans = 0
    for i in range(0, n - 1):
        ans = max(ans, LPS[0][i] * LPS[i + 1][n - 1])
    return ans



def getsubstrings(s):
    result = []
    for y in range(len(s) -1, 0, -1):
        if s[y] not in result:
            result.append(s[y])
        for x in combinations(s, y):
            #if ''.join(x) == ''.join(x)[::-1]:
            if isPalindrome(x):
                newstr = ''.join(x)
                if newstr not in result:
                    result.append(newstr)
    return result


def isPalindrome(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False
    else:
        return isPalindrome(s[1:-1])


def getScore1(s):
    # Write your code here
    stringList = getsubstrings(s)
    #print(stringList)
    #zipped_allSubStr = zip(allsubstr, allsubstrPos)
    #palsubstr = [(substr, substrPos, len(substr)) for substr, substrPos in zipped_allSubStr if isPalindrome(substr)]
    #stringList = [(substr, substrPos, len(substr)) for substr, substrPos in zipped_allSubStr]
    #stringList = sorted(palsubstr, key=lambda x: x[2])
    #stringList.reverse()
    maxPrdt = 0
    i = 0
    for substr in stringList:
        startPos = s.index(substr[0])
        length = len(substr)
        if length == 1:
            endPos = startPos
        else:
            endPos = s.rindex(substr[-1])
        i += 1
        for j in range(i, len(stringList)):
            secondStartPos = s.index(stringList[j][0])
            secondlength = len(stringList[j])
            if secondlength == 1:
                secondEndPos = secondStartPos
            else:
                secondEndPos = s.rindex(stringList[j][-1])

            if (endPos < secondStartPos and endPos < secondEndPos) or (
                    startPos > secondStartPos and startPos > secondEndPos):
                prdt = length * secondlength
                if prdt > maxPrdt:
                    maxPrdt = prdt

    return maxPrdt


res = getScore('attract')
print(res)
res = getScore('acdapmpomp')
print(res)
res = getScore('axbawbaseksqke')
print(res)
r = getScore("axbawbaseksqkeacdapmpompacdapmpomp")
print(r)
import cProfile
cProfile.run('getScore("acdapmpomp")')
cProfile.run('getScore("acdapmpompacdapmpomp")')
#cProfile.run('getScore("axbawbaseksqkeacdapmpompacdapmpomp")')