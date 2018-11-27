def formatNumber(S):
    S = S.replace('-','')
    S = ''.join(S.split())
    length = len(S)
    #temp = ''
    
    words = []

    for i in range(length):
        cur = S[0:i]
        remaining = S[i+1:length]
        word = helperFormat(cur, i, remaining,S)         
    words.append(word)


def helperFormat(cur,i, remaining,S):    
    #choose/explore(add/delete)/unchoose
    if i > len(S):
        return False
    else:
        for j in range(len(remaining)):
            cur = cur + remaining[j]
            cur.r

            helperFormat(cur,j,remaining)
            #helperFormat(cur, 0, remaining,S)     


s = 'khera'
i = 2
print(s[-i])
print(s[-1])
print(s[:2])
print(s[0:2])
print(s[1:2])


import re
example = 'abcdefabcdefabcdefg'
for match in re.finditer('abc', example):
    print match.start(), match.end()

s = 'attract'
s.index('a')
s.index('tt')
s.find('tt')
t = 'ara'
print(t[0])
s.find(t)

if s.find(t) == -1:
    z = s.find(t[0])
z