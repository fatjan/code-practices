def checkGroup(word, group):
    if word == '':
        return False
    cond = True
    for i in word:
        if i in group:
            continue
        else:
            cond = False
            break
    return cond

def groupAnagrams(strs):
    if len(strs) == 1:
        return [[strs[0]]]
    groups = [strs[-1]]
    isi_group = [[]]
    found = False
    for i in range(len(strs)-1, -1, -1):
        for j in range(len(groups)):
            print(isi_group)
            if checkGroup(strs[i], groups[j]):
                isi_group[j].append(strs[i])
                break
            else:
                found = False
                for k in range(len(groups)):
                    if checkGroup(strs[i], groups[k]):
                        found = True
                        break
                if found == False:
                    groups.append(strs[i])
                    isi_group.append([strs[i]])
    return isi_group

# print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(groupAnagrams([""]))
