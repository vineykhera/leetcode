"""
     100 4  200 1 3 2
100 
4
200
1
3
2

6:35
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        ans = 0
        # visited = set(nums)
        maxnum = float('-inf')
        
        if not nums: 
            return 0
        
        for n in numset:
            # saven = n
            
            if n-1 not in numset:
                ans = 1
                saven = n

                while saven+1 in numset:
                    ans +=1
                    saven = saven+1
                    # visited.add(n)

                maxnum = max(ans, maxnum)
          
        return maxnum
            
            
                
            
        
        #         cnt = Counter(nums)
#         print(cnt)
#         maxnum = float('-inf')
#         minnum = float('inf')
#         ans = [minnum, maxnum]
#         visited = set()
        
#         def checknumber(checknum, cnt, ans):
#             minnum = ans[0]
#             maxnum = ans[1]
#             print('checknum', checknum, minnum, maxnum, visited)
#             if checknum in cnt and n not in visited:
#                 minnum  = min(checknum, minnum) 
#                 maxnum  = max(checknum, maxnum)
#                 visited.add(n)

#                 if checknum-1 in cnt:
#                     checknumber(checknum-1, cnt,[minnum, maxnum])
#                 if checknum+1 in cnt:
#                     checknumber(checknum+1, cnt, [minnum, maxnum])
                
#         for n in nums:
#             checknumber(n, cnt, [minnum, maxnum])
        
#         return (ans[1]-ans[0])+1