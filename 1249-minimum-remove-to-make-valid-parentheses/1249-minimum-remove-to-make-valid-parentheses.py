class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        indxtoremove = set()
        for i, c in enumerate(s):
            if c == '(':
                st.append((c,i))
                # indxtoremove.add(i)                
            elif c == ')':
                if len(st) > 0 and st[-1][0] == '(':
                    st.pop()
                else:
                    st.append((c,i))
                    # indxtoremove.add(i)
            else:
                continue
                
        res = []
        # print(st)
        
        for i in range(len(st)):
            indxtoremove.add(st[i][1]) 

        for i, c in enumerate(s):
            # print(i,indxtoremove)
            if i not in indxtoremove:
                res.append(c)
    
        return "".join(res)
    

            