num = int(input())
colors = [[],[],[],[],[]]
for _ in range(num):
    new_line = input()
    items = new_line.split(' ')
    if items[1] == 'red':
        for i in range(len(items)):
            if i >= 2:
                colors[int(items[i])-1].append('r')
    elif items[1] == 'green':
        for i in range(len(items)):
            if i >= 2:
                colors[int(items[i])-1].append('g')
    elif items[1] == 'blue':
        for i in range(len(items)):
            if i >= 2:
                colors[int(items[i])-1].append('b')
    elif items[1] == 'yellow':
        for i in range(len(items)):
            if i >= 2:
                colors[int(items[i])-1].append('y')
    elif items[1] == 'white':
        for i in range(len(items)):
            if i >= 2:
                colors[int(items[i])-1].append('w')

for i in range(len(colors)):
    if list(set(colors[i])) != colors[i]:
        print('UNDEFINED')
    elif len(colors[i]) > 1:
        print('YES')
    else:
        print('NO')
    
