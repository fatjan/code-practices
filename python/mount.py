n = int(input())
space = input()
arr = []
for _ in range(n):
    num_step = int(input())
    new_line = input()
    steps = [int(x) for x in new_line.split(" ")]
    if steps.count(1) == 0:
        arr.append('-1 -1')
    else:
        highest = max(steps)
        index = steps.index(highest)
        to_input = str(highest) + ' ' + str(index)
        arr.append(to_input)
    space = input()

for i in range(1,len(arr)+1):
    kata = 'Case #' + str(i) + ': ' + arr[i-1]
    print(kata)
