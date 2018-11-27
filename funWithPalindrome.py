import math

def getPalindromicSubSequences(s='attract'):
    allsubstr, allsubstrPos = get_all_substrings(s)
    zipped_allSubStr = zip(allsubstr, allsubstrPos)
    #print(allsubstrPos)
    #palsubstr = list(filter(lambda substr: isPalindrome(substr), allsubstr))
    #palsubstr = filter(lambda subStr : isPalindrome(subStr), allsubstr)
    #[Euclidean_norm(*x,*y,*z) for x,y,z in zip(x_list, y_list, z_list)]S
    palsubstr = [(substr, substrPos, len(substr)) for substr, substrPos in zipped_allSubStr if isPalindrome(substr)]
    # xVar, yVar = zip(*xyFiltered)


    #print('palsubstr is')
    #print(palsubstr)
    #length_palsubstr = list(map(lambda substr: len(substr), palsubstr))
    #print('length of palsubstr is')
    #print(length_palsubstr)
    #print('start_palsubstr')
    #start_palSubstr = list(map(lambda substr: getStartIndex(substr,s), palsubstr))
    #print(start_palSubstr)
   
    #print('end_palsubstr')
    #end_palSubstr = list(map(lambda substr: getEndIndex(substr,s), palsubstr))
    #print(end_palSubstr)
    
    #zipped_pal = zip(palsubstr, length_palsubstr, start_palSubstr, end_palSubstr) 
    #sorted_by_value = sorted(zipped_pal, key=lambda x: x[1])
    sorted_by_value = sorted(palsubstr, key=lambda x: x[2])
    sorted_by_value.reverse()
    #sorted_by_value = sorted(dict_pal.items(), key=lambda x: x[1])
    print('sorted list is')
    print(sorted_by_value)
    #max1 = max(sorted_by_value, key=lambda x:x[2])
    #print(max1)
    max = getScore(sorted_by_value)
    return max

def getStartIndex(substr,s):
    if s.find(substr) == -1:
        return s.find(substr[0])
    else:
        return s.find(substr)

def getEndIndex(substr,s):
    if s.find(substr) == -1:
        return s.rfind(substr[-1])
    else:
        if len(substr) > 1:
            return s.find(substr) + len(substr) - 1
        else:
            return s.find(substr)


def get_all_substrings(chars):
    result = []
    resultPos = []
    binary = []
    length = len(chars)
    total = int(math.pow(2, length))

    for i in range(1,total):
        binaryNum = format(i, "b")
        tempSubStr = []
        tempSubStrPos = []

        while (len(binaryNum) < length):
            binaryNum = "0" + binaryNum
        binary.append(binaryNum)

        for j in range(0, length):
            if "1" in binaryNum[j]:
                tempSubStr.append(chars[j])
                tempSubStrPos.append(j)

        newstr = ''.join(tempSubStr)
        #result.append([newstr, len(newstr), tempSubStrPos[0], tempSubStrPos[-1]]) 
        resultPos.append([tempSubStrPos[0], tempSubStrPos[-1]]) 
        #if isPalindrome(newstr):
        #if newstr not in result:
        result.append(newstr)
    return result, resultPos


def isPalindrome(s):
    if len(s) <= 1:
        return True

    if s[0] == s[-1] and isPalindrome(s[1:-1]):
        return True
    else:
        return False


def getScore(sorted_by_value):
    # Write your code here
    maxPrdt = 0
    i = 0
    for substr, pos, length in sorted_by_value:
        startPos = pos[0]
        endPos   = pos[1]
        i += 1
        for j in range(i,len(sorted_by_value)):
            secondStartPos = sorted_by_value[j][1][0]
            secondEndPos   = sorted_by_value[j][1][1]
            secondlength   = sorted_by_value[j][2]
            if (endPos < secondStartPos and endPos < secondEndPos) or (startPos > secondStartPos and startPos > secondEndPos):
                prdt = length * secondlength 
                if prdt > maxPrdt: 
                    maxPrdt = prdt

    return maxPrdt

#print(isPalindrome('atta'))

#print(isPalindrome('abacabab'))
#print(isPalindrome('abacaba'))
#print(getPalindromicSubSequences(), len(getPalindromicSubSequences()))
res = getPalindromicSubSequences()
print(res)
res = getPalindromicSubSequences('acdapmpomp')
print(res)