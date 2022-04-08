"""
time 6:32
start test 6:55
wrong
7:12am - return issues, check solution
7:44 still same issue after checking solutions

"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
            rows, cols = len(board), len(board[0])
            path = set()

            def dfs(r, c, i):
                if i == len(word):
                    return True
                if r < 0 or r >= rows or c <  0 or c >= cols or board[r][c] != word[i] or (r,c) in path:
                    return False

                path.add((r,c))
                res = dfs(r + 1, c, i+1) or dfs(r - 1, c, i+1) or dfs(r, c + 1, i+1) or dfs(r , c - 1, i + 1)
                path.remove((r,c))
                return res

            for r in range(rows):
                for c in range(cols):
                    if dfs(r, c, 0): return True

            return False
    
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         r = len(board)
#         c = len(board[0])
#         visited = set()
        
#         dircs = [(1,0), (-1,0), (0,1), (0,-1)]
        
#         def isvalidcord(r,c,i,j,word, wordindx):
#             if i >= 0 and i < r and j >= 0 and j < c and (i,j) not in visited and board[i][j] == word[wordindx]:
#                 return True
#             else:
#                 return False
        
#         def helper(board, r,c, i, j, word, wordindx):
#             # print(wordindx)
#             if wordindx == len(word):
#                 return True

#             if i < 0 or i >= r or j < 0 or j >= c or (i,j) in visited or board[i][j] != word[wordindx]:
#                 return False
            
#             visited.add((i,j))
#             for x,y in dircs:
#                 if helper(board, r,c,i+x,j+y, word, wordindx+1):
#                     return True
#             visited.remove((i,j))
#             # return False
        
#         for i in range(r):
#             for j in range(c):
#                 if helper(board, r,c,i,j, word, 0):
#                     return True
        
#         return False
                    