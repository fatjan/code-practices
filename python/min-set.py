def minSetSize(arr):
    print(len(arr))
    print(list(set(arr)))
    print(len(list(set(arr))))
    if arr.count(arr[0]) == len(arr) or len(arr) == 2:
        return 1
    if list(set(arr)) == arr:
        return len(arr) // 2
    if len(list(set(arr))) == len(arr):
        return len(arr) // 2
    elif len(list(set(arr))) > len(arr)//2:
        return len(list(set(arr))) - len(arr) // 2
    else:
        return len(list(set(arr))) // 2


print(minSetSize([72, 18, 36, 6, 12, 97, 41, 82, 44, 75, 82, 42, 75, 48, 63, 9, 61, 50, 11, 91, 24, 26, 3, 65, 31, 67, 15, 76, 54, 59, 4, 27, 33, 26, 17, 60, 100, 19, 90, 6, 80,
      82, 48, 70, 85, 99, 69, 2, 78, 94, 15, 29, 75, 17, 9, 79, 99, 88, 26, 73, 88, 100, 9, 95, 2, 56, 63, 31, 25, 40, 8, 100, 56, 44, 36, 42, 21, 96, 63, 38, 96, 78, 60, 22, 21, 81]))
# print(minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]))
