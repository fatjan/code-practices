def migratoryBirds(arr):
    dist = []
    amount = []
    curr_most = 0
    ind_most = []
    for i in range(len(arr)):
        if arr[i] not in dist:
            dist.append(arr[i])
            amount.append(arr.count(arr[i]))
            if curr_most < amount[len(amount) - 1]:
                ind_most.append(amount[len(amount)-1])
                curr_most = amount[len(amount) - 1]
                ind_most = ind_most[1:]
            elif curr_most == amount[len(amount) - 1]:
                ind_most.append(amount[len(amount) - 1])
    print(dist)
    print(amount)
    print(ind_most)
   
    # maxie = []
    # for a in range(len(amount)):
    #     if amount[a] == max(amount) and amount[a] not in maxie:
    #         maxie.append(a)
    # last = []
    # if len(maxie) == 1:
    #     return dist[maxie[0]]
    # else:
    #     for i in range(len(maxie)):
    #         last.append(dist[maxie[i]])
    #     res = sorted(last)
    # return res[0]

print(migratoryBirds([1, 24, 24, 6, 2, 2, 9, 9, 9, 19, 24]))
