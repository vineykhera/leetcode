class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        # mxword = 0
        # for st in sentences:
        #     mxword = max(mxword, len(st.split(" ")))
        # return mxword
        
        # return max(len(st.split()) for st in sentences)
        
        return max(st.count(" ")+1 for st in sentences)
        
        # return 
        
