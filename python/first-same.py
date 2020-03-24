def firstDuplicate(a):
    b = []
    for i in range(len(a)):
        print(a[i])
        if a[i] not in b:
            b.append(a[i])
            print(b)
        else:
            return a[i]
    return -1


print(firstDuplicate([2, 1, 3, 5, 3, 2]))
