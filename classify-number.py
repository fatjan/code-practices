def mengelompokkanAngka(arr):
    genap = []
    ganjil = []
    multiple3 = []
    outside = []
    for num in arr:
        if num % 2 is 0:
            genap.append(num)
        elif num % 2 is not 0:
            ganjil.append(num)
        if num % 3 is 0:
            multiple3.append(num)
    outside.append(genap)
    outside.append(ganjil)
    outside.append(multiple3)
    return outside

print(mengelompokkanAngka([2, 4, 6]))
print(mengelompokkanAngka([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(mengelompokkanAngka([100, 151, 122, 99, 111]))
print(mengelompokkanAngka([]))





