"""
 9:04           



"""
# class Solution:
#     def letterCasePermutation(self, s: str) -> List[str]:
#         result = []
#         def backtrack(curstr, i):
#             if len(curstr) == len(s):
#                 result.append(curstr)
            
#             #i learnt loop isnt needed, no needed to pass result in backtrack as well in func arguments
#             # for i in range(start, len(s)):
#                 # if s[i].isalpha():
#                 #     backtrack(s[:i]+s[i].swapcase()+s[i+1:],i+1)
#                 # backtrack(s,i+1)
#             if s[i].isalpha():
#                 backtrack(curstr+s[i].swapcase(),i+1)
#             backtrack(curstr+s[i],i+1)
                    
            
#         backtrack("",0)
#         # backtrack("",0, result)
#         return result


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        def backtrack(curstr, i):
            if len(curstr) == len(s):
                result.append(curstr)
            else:
                if s[i].isalpha():
                    backtrack(curstr+s[i].swapcase(),i+1)
                backtrack(curstr+s[i],i+1)
                    
            
        backtrack("",0)
        return result