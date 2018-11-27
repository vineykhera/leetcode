from itertools import combinations
import math


def get_all_substrings(chars):
    result = []
    resultPos = []
    binary = []
    length = len(chars)
    total = int(math.pow(2, length))

    for i in range(1, total):
        tempSubStr = []
        tempSubStrPos = []

        binaryNum = bin(i)[2:].zfill(length)

        # binaryNum = format(i, "b")
        # binaryNum = format(i, f"0{length}b")
        # while (len(binaryNum) < length):
        #    binaryNum = "0" + binaryNum
        binary.append(binaryNum)

        for j in range(0, length):
            if "1" in binaryNum[j]:
                tempSubStr.append(chars[j])
                tempSubStrPos.append(j)

        newstr = ''.join(tempSubStr)
        resultPos.append([tempSubStrPos[0], tempSubStrPos[-1]])
        result.append(newstr)
    return result, resultPos


def isPalindrome(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False
    else:
        return isPalindrome(s[1:-1])


def getScore(s):
    # Write your code here
    allsubstr, allsubstrPos = get_all_substrings(s)
    zipped_allSubStr = zip(allsubstr, allsubstrPos)
    palsubstr = [(substr, substrPos, len(substr)) for substr, substrPos in zipped_allSubStr if isPalindrome(substr)]
    sorted_by_value = sorted(palsubstr, key=lambda x: x[2])
    sorted_by_value.reverse()
    maxPrdt = 0
    i = 0
    for substr, pos, length in sorted_by_value:
        startPos = pos[0]
        endPos = pos[1]
        i += 1
        for j in range(i, len(sorted_by_value)):
            secondStartPos = sorted_by_value[j][1][0]
            secondEndPos = sorted_by_value[j][1][1]
            secondlength = sorted_by_value[j][2]
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

import cProfile
cProfile.run('getScore("acdapmpomp")')