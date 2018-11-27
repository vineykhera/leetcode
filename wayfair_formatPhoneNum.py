def formatPhoneNumber(S):
    #S.replace(' ','')
    S= S.replace("-","")
    S = ''.join(S.split())
    tempS = ''
    ans = ''

    num = 3
    length = len(S)
    rem = length % 3
    print(S,length, rem)
    for i in range(0,length,num):
        left = length - i
        if left > 4:
            tempS = S[i:i+num]
            i += 3
            if left > 1: 
                tempS = tempS + '-'
        else:
            num = 2
            tempS = S[i:i+num]
            i += 2
            if left > 1: 
                tempS = tempS + '-'
        ans = ans + tempS
    return ans

phone = formatPhoneNumber('00-44  48 55 55 8361')
print(phone)

phone = formatPhoneNumber('00-4448 55 55 836')
print(phone)
