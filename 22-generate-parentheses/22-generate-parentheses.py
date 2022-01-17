"""
7:30
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def helper(left, right, cur, result):
            if len(cur) == 2*n and left == right:
                result.append(cur)
            
            if left >= 0 and left < n:
                helper(left+1, right, cur +"(", result)
            if right < left and right < n:
                helper(left, right+1, cur +")", result)
                        
            
        helper(0,0, "", result)
        return result
        