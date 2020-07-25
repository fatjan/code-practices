from itertools import combinations 
import itertools

cases = int(input())
for _ in range(cases):
    new_line = input()
    l1 = [int(x) for x in new_line.split(" ")]
    n = l1[0]
    arr = []
    for i in range(n):
        arr.append(i)
    arr_tuple = tuple(arr)
    k = l1[1]
    com = [p for p in itertools.combinations_with_replacement(arr, k)]
    total = len(com)
    dist_star = com.count(arr_tuple)
    upper = total - dist_star
    print(upper, total)