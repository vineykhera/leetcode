class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for st in strs:
            ordst = sorted(st)

            ordst = "".join(ordst)
   
            dic[ordst].append(st)
        out = []
        for v in dic.values():
            out.append(v)
        return out
