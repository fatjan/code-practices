import math
cases = int(input())
result = []
for i in range(cases):
    line = input()
    items = line.split(' ')
    vol = 1
    for item in items:
        vol *= int(item)
    for side in range(1,vol+1):
        hasil = vol / (side ** 3)
        if hasil == math.ceil(hasil):
            result.append(side)
    print('hasil ', hasil)
    max_side = max(result)
    total = vol // (max_side ** 3)
    print(max_side, total)