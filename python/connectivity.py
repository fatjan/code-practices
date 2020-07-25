line = input()
items = [int(x) for x in line.split(" ")]
cases = items[0]
nums = items[1]
arr = []
for i in range(1,nums+1):
    inside = [i]
    arr.append(inside)
arr_before = [arr]
import collections

def connect(start, end):
    take = []
    for i in range(len(arr)):
        if start-1 <= i < end-1:
            for j in range(len(arr[i])):
                take.append(arr[i][j])
            arr[i] = []
        take.sort()
        take.reverse()
        if i == end-1:
            for num in take:
                arr[i].insert(0, num)
    return arr

def disconnect(start, end):
    sambung = arr[end-1]
    take_out = sambung[:len(sambung)-1]
    move_out = take_out[0]
    arr[end-1].remove(move_out)
    arr[start-1] = [start]

last_connect = []

for i in range(1,cases+1):
    new_line = input()
    comps = [x for x in new_line.split(" ")]
    kata = comps[0]
    if kata == 'PUSH':
        start = int(comps[1])
        end = int(comps[2])
        arr = connect(start, end)
        last_connect.append(start)
        last_connect.append(end)
        num_comps = len(arr) - arr.count([])
        print(num_comps)
    else:
        disconnect(last_connect[-2], last_connect[-1])
        num_comps = len(arr) - arr.count([])
        print(num_comps)

