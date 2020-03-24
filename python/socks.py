def sockMerchant(n, ar):
    ray = ar
    count = 0
    for i in range(len(ray)):
        if i + 1 > len(ray):
            return count
        else:
            j = i+1
            for j in range(len(ray)):
                if ray[i] == ray[j]:
                    count += 1
                    ray.pop(j+1)
                    print('ray after 1',ray)
                    ray = ray[1:]
                    print('ray after 2', ray)
                    unique = set(ray)
                    break


print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
print(sockMerchant(10, [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]))
