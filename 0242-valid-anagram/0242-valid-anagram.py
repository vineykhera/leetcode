class Solution(object):
    def isAnagram(self, s1, s2):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        c1 = collections.Counter(s1)

        for c in list(s2):
            if c in c1:
                c1[c] -= 1
            else:
                return False


        # print(c1)
        for k, v in c1.items():
            if v != 0:
                return False
        return True
