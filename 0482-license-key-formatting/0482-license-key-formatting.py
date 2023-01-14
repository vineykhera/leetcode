class Solution:
    def licenseKeyFormatting1(self, s: str, k: int) -> str:
        arr = s.split("-")
        news = "".join(arr)
        # print(news)
        l = 0
        out = ""
        for i in range(len(news)-1,-1,-1):
            out = news[i] + out
            l += 1
            if l == k and i > 0:
                out = "-" + out
                l = 0
        return out.upper()
    
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        arr = s.split("-")
        news = "".join(arr)
        # print(news)
        l = 0
        n = len(news)
        out = ""
        grp1size = n % k
        if grp1size > 0:
            out = news[:grp1size]
        # print(grp1size)
        for i in range(grp1size,n,k):
            if len(out) > 0:
                out += "-"
            out += news[i:i+k]
      
        return out.upper()