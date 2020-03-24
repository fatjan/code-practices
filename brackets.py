def isBalanced(s):
    trueb = '{[('
    for i in range(len(s) // 2):
        if s[i] not in trueb:
            return 'NO'
    for i in range(len(s)):
        if s[i] == '{' and s[-(i+1)] != '}':
            return 'NO'
        elif s[i] == '[' and s[-(i+1)] != ']':
            return 'NO'
        elif s[i] == '(' and s[-(i+1)] != ')':
            return 'NO'
    return 'YES'

print(isBalanced('{{[[((()))]]}}'))
print(isBalanced('{{)[](}}'))
