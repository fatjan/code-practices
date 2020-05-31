cases = int(input())
for _ in range(cases):
    line = input()
    line = line.split(' ')
    a = int(line[0])
    b = int(line[1])
    total = 0
    for i in range(a,b+1):
        i = str(i)
        if len(i) % 2:
            if i[:len(i)//2] == i[len(i):-len(i)//2:-1]:
                total += 1
        else:
            if i[:len(i)//2] == i[len(i):-len(i)//2-1:-1]:
                total += 1
    print(total)