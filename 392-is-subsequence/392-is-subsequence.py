"""
    ahbgdc
  a 111111 
  b 112222 
  c 112223
 2 pointer

"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        if not s:
            return True
        if s and not t:
            return False
        # if len(s)
        while j <= len(t) - 1 and i <= len(s)-1 :
            print(i,j)
            if t[j] == s[i]:
                # print("match",s[i], j)                
                i += 1
            j += 1
        # print("at end", i,j)
        return True if len(s) == i else False