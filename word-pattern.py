
def wordPattern(pattern, str):
    if pattern.count(pattern[0]) == len(pattern):
        if str.count(str[0]) == len(str):
            return True
    if len(list(set(pattern))) == len(list(set(str))):
            return True
    str_s = str.split(' ')
    pat_list = []
    pat_num = []
    str_num = []
    str_list = []
    for i in range(len(pattern)):
        if pattern[i] not in pat_list:
            pat_list.append(pattern[i])
            pat_num.append(i)
            print(pat_num)
        else:
            for j in range(len(pattern) - i):
                if pattern[j] == pattern[i]:
                    pat_num.append(pat_num[j])
        if str_s[i] not in str_list:
            str_list.append(str_s[i])
            str_num.append(i)
        else:
            for k in range(len(str_s) - i):
                if str_s[k] == str_s[i]:
                    str_num.append(str_num[j])
    if len(pat_list) != len(str_list):
        return False
    elif str_num != pat_num:
        return False
    return True
    


print(wordPattern("abba", "dog cat cat fish"))
