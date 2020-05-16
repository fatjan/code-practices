def find_nb(m):
    # your code
    # for i in range(2,m):
    #     n = i
    #     sum = 0
    #     while sum <= m:
    #         sum += n ** 3
    #         n -= 1
    #         if n == 1:
    #             sum += 1
    #             break
    #     if sum == m:
    #         return i
    #     elif sum > m:
    #         return -1
    # for i in range(2,m):
    i = 2
    n = i
    sum = 0
    while sum < m:
        sum += n ** 3
        n -= 1
        if n == 1:
            sum += 1
            if sum == m:
                return i
            if sum > m:
                return -1
            sum = 0
            i += 1
            n = i

print(find_nb(1071225))
print(find_nb(26825883955641))
print(find_nb(135440716410000))
