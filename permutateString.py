def permutateString(s):
    words = []
    chosen = ''
    word = permuteHelper(chosen, s)
    words.append(word)
    print(words)


def permuteHelper(chosen, s):
    #print(chosen, s)
    if s == '':
        print(chosen)
    else:
        #add(choose)/explore/delete(unchoose)
        for i, c in enumerate(s):
            #choose
            chosen += s[i]
            remaining = s[i+1:len(s)]
            #explore
            #print('one', chosen, remaining, s)
            permuteHelper(chosen, remaining)
            #unchoose
            chosen = chosen[0:len(chosen)-1]
            #print('two', chosen, s)
            #return chosen


def easy_permute(s):
    if len(s) == 1:
        return [s]
    else:
        result = []
        for i, c in enumerate(s):
            result += [c+p for p in easy_permute(s[:i] + s[i+1:])]
        return result


permutateString('viney')
print('new code')
print('new code')
print('new code')
print(easy_permute('viney'))