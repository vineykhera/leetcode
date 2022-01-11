"""
seen - e a t b a





"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         dic = collections.defaultdict(list)
#         for s in strs:
#             dic[tuple(sorted(c for c in s))].append(s)
        
        
#         return [values for values in dic.values()]

        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()