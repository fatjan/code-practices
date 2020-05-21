tcases = int(input())
for _ in range(tcases):
    line1 = input()
    l1 = line1.split(' ')
    n = int(l1[0])
    n_move = int(l1[1])
    line2 = input()
    arr = line2.split(' ')
    move = 0
    while move < n_move:
        min_v = min(arr)
        for j in range(len(arr)):
            if arr[j] == min_v:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                move += 1
                break
    print(' '.join([str(elem) for elem in arr]))