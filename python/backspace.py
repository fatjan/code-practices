def removeHash(str):
    s = ''
    s_removed = str
    while '#' in s_removed:
        for i in range(len(s_removed)):
            if i == len(s_removed) - 1 and s_removed[i] != '#':
                s += s_removed[i]
            if i != len(s_removed) - 1:
                if s_removed[i+1] != '#' and s_removed[i] != '#':
                    s += s_removed[i]
            if s_removed[i] == '#' and s_removed[i - 1] == '#' and i != 0:
                s += s_removed[i]
        s_removed = s
        s = ''
    return s_removed

def backspaceCompare(S, T):
    if removeHash(S) == removeHash(T):
        return True
    return False


print(backspaceCompare('ab#c','ad#c'))


# s = s[0:len(s)-1] for pop from string
