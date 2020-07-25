n = int(input())
for i in range(1,n+1):
    num_step = int(input())
    new_line = input()
    steps = [int(x) for x in new_line.split(" ")]
    print(steps)
    if steps.count(1) == 0:
        print('Case #%d: -1 -1' % i )
    else:
        highest = max(steps)
        index = steps.index(highest)
        print('Case #%d: %d %d' % (i, highest, index) )