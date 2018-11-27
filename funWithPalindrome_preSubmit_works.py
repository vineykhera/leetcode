
from itertools import combinations

def getsubstrings(s):
    result = []
    for y in range(len(s)-1, 0, -1):
        result.append((s[y], [s.index(s[y]), s.index(s[y])]))
        for x in combinations(s, y):
            if ''.join(x) == ''.join(x)[::-1]:
                newstr = ''.join(x)
                result.append((newstr, [s.index(x[0]), s.rindex(x[-1])]))
    return result


def getScore(s):
    stringList = getsubstrings(s)
    maxPrdt = 0
    i = 0
    for substr, pos in stringList:
        startPos = pos[0]
        endPos = pos[1]
        length = len(substr)
        i += 1
        for j in range(i, len(stringList)):
            secondStartPos = stringList[j][1][0]
            secondEndPos = stringList[j][1][1]
            secondlength = len(stringList[j][0])
            if (endPos < secondStartPos and endPos < secondEndPos) or (
                    startPos > secondStartPos and startPos > secondEndPos):
                prdt = length * secondlength
                if prdt > maxPrdt:
                    maxPrdt = prdt

    return maxPrdt
