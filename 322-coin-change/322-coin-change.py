# """--
# top down :
# 1 + min(f(n-5), f(n-1), f(n-2))
# add memoization

# for bottom up:
# 1 2 3 4 5 6 7  8 9 10 11
# 1 1 2  

# = if n exits in coins then 1 
# else:
#     1 + min(n-c1, n-c2, n-c3)


#    1 2 5
# 1
# 2
# 5

# """


# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         def helper(coins, amount, memo):
#             coinset = set(coins)
#             # print(amount, memo)
#             if amount < 0:
#                 return math.inf
#             if amount == 0:
#                 return 0
                
#             if amount in coinset:
#                 memo[amount] = 1
#                 return 1
#             if amount in memo:
#                 return memo[amount]
            
#             mintemp = float('inf')
#             for c in coins:
#                 if amount - c > 0:
#                     if amount - c in memo:
#                         temp = memo[amount - c]
#                     else:
#                         temp = helper(coins, amount-c, memo)
#                     mintemp = min(mintemp, temp)
                    
#             memo[amount] = 1 + mintemp
#             return memo[amount]

#         memo = dict()
#         ans = helper(coins, amount, memo) 
#         if ans != math.inf: 
#             return ans
#         else:
#             return -1
#         # print(memo)
#         # return memo[amount]

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:            
#         def coinChangeInner(rem, cache):
#             if rem < 0:
#                 return math.inf
#             if rem == 0:                    
#                 return 0       
#             if rem in cache:
#                 return cache[rem]
            
#             cache[rem] = min(coinChangeInner(rem-x, cache) + 1 for x in coins)                         
#             return cache[rem]      
        
#         ans = coinChangeInner(amount, {})
#         return -1 if ans == math.inf else ans     

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:   
        
        dp = [math.inf] * (amount+1)
        dp[0] = 0
        
        for c in coins:
            for x in range(c, amount+1):
                dp[x] = min(dp[x],dp[x-c] + 1)
        
        return -1 if dp[-1] == math.inf else dp[-1]