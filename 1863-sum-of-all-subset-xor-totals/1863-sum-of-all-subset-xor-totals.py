
"""
7:41
7:47
                      5,1,6
            5,1      1,6          5,6
         5     1     1    6       5    6
                
"""
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result =list()
        self.output = 0
        
        def subsets(start, result):
            cursum = 0
            # print("Subset", result)
            for n in result:
                cursum ^= n
            self.output += cursum

            for i in range(start,len(nums)):
                result.append(nums[i])
                subsets(i+1, result)
                result.pop()
            
        subsets(0, result)
        # print(result)
        return self.output
    
    

#         self.res = 0
        
#         def dfs(path, start):
#             curSum = 0
#             print(path)
#             for n in path:
#                 curSum = curSum ^ n
#             self.res += curSum
            
#             for i in range(start, len(nums)):
#                 num = nums[i]
#                 path.append(num)
#                 dfs(path, i + 1)
#                 path.pop()
            
#         dfs([], 0)    
#         return self.res

