"""
42:11, 1, 79 =53,43,121
11: 1, 79 = 12,90
1, 79 = 80
97
24:11,1,97 = 
79

"""
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            s = n - int(str(n)[::-1])
            if s not in d:
                d[s] = 1
            else:
                d[s] += 1
        out = 0
        for s in d.values():
            out += s * (s-1)//2
        return out % ((10**9) + 7)
            