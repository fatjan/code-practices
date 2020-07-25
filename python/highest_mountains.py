n = int(input())
space = input()
for i in range(1,n+1):
    num_step = int(input())
    new_line = input()
    steps = [int(x) for x in new_line.split(" ")]
    if steps.count(1) == 0:
        print(f'Case #{i}: -1 -1')
    else:
        highest = max(steps)
        index = steps.index(highest)
        print(f'Case #{i}: {highest} {index}')
    space = input()
    
