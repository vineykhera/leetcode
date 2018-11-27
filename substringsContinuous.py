for i, c in enumerate(s):
    if c not in result:
        result.append(c)
    else:
        if c + c not in result:
            result.append(c + c)

for i in range(l):
    for j in range(i, l):
        for k in range(1, 3):
            substr = s[i:j + 1:k]
            if isPalindrome(substr, result):
                result.append(substr)
