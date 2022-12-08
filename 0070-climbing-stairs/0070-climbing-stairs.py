# class Solution:
#     def climbStairs(self, n: int) -> int:
#         one = 1
#         two = 1
#         for i in range(n-1):
#             temp = one
#             one = one + two
#             two = temp
#         return one

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        
        prev, curr = 1, 2
        for _ in range(n - 2):
            prev, curr = curr, prev + curr

        return curr
