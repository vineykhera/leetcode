#abcabcd : abc, bca, cab, abcd


class Solution:
    def length_max_substr(self, s):
        j = 0
        maxlen = 0
        results = {}
        if s == '':
            return 0
        if len(s) == 1:
            return 1
        for i in range(1, len(s)):
            if s[i] == s[j]:
                result = s[j:i]
                length = i - j
                results.update({result:length})
                j = j + 1
            elif s[i] in s[j:i]:
                result = s[j:i]
                length = i - j
                results.update({result: length})
                j = length - 1
            else:
                if i == len(s) - 1:
                    result = s[j:]
                    results.update({result:i-j+1})
        maxlen = max(results.values())
        return (maxlen, results)


sol = Solution()
print(sol.length_max_substr('abcabcbb'))
print(sol.length_max_substr('dvdf'))
print(sol.length_max_substr('pwwkew'))
print(sol.length_max_substr('bbbbb'))
print(sol.length_max_substr('ohvhjdml'))
print(sol.length_max_substr(''))
