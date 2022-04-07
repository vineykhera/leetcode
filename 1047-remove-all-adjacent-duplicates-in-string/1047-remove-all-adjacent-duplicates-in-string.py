"""
10pm

abbaca
ij
10:10
"""
class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        last = ""
        for c in s:
            # print(st)
            if len(st) == 0:
                st.append(c)
            else:
                last = st[-1]
                # print(last, st[-1])
                if last == c:
                    st.pop()
                else:
                    st.append(c)
        # print(st)
        return "".join(st)