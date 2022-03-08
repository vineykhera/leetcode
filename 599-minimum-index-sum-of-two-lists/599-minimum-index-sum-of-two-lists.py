class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic = {}
        newdic = {}
        
        for i,s in enumerate(list1):
            dic[s] = i
        
        # print(dic)
        
        for j,s in enumerate(list2):
            if s in dic:
                newdic[s] = dic[s] + j
            else:
                dic[s] = j
        
        # print(newdic)
        minval = float('inf')
        ans = []

        for k,v in newdic.items():
            # print(k,v)
            if v <= minval:
                minval = v

        for k,v in newdic.items():
            # print(k,v)
            if v == minval:
                ans.append(k)
 
        # print(ans)
        # print("".join(ans))
        return ans
        