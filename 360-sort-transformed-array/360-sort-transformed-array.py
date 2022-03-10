class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        result = []
        for n in nums:
            temp = a*n**2 + b*n + c
            result.append(temp)
        result = sorted(result)
        return result