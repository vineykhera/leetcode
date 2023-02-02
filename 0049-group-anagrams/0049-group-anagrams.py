class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for st in strs:
            dic["".join(sorted(list(st)))].append(st)
        return dic.values()

