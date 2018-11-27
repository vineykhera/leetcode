chars = []
allsubstr = []
palsubstr = []
l = len(s)
for i in range(l):
    if s[i - 1] != s[i]:
        chars.append(s[i])
# print(chars)
# print(''.join(chars))


#leetCode_powerSet.py
n = 6
nbin = format(n, f"0{n}b")
print(n,nbin)