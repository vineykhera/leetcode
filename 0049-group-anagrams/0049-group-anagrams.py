class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for st in strs:
            key = tuple(sorted(collections.Counter(st).items()))
            # print(key)
            dic[key].append(st)
        return dic.values()

