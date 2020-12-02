def hitung(num):
    i = 0
    s = 0
    while i < len(num):
        s += num[i]
        i += 1
    return s

print(hitung([5, 7, 8, 3]))