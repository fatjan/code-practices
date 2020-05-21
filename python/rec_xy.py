line = input()
line = line.split(' ')
x = int(line[0])
y = int(line[1])
def recursive(x, y):
    if x == 0:
        y += 1
        return y
    elif x > 0 and y == 0:
        return recursive(x-1, 1)
    elif x > 0 and y > 0:
        return recursive(x-1, recursive(x, y-1))

a = recursive(1, 100)
print(str(a)[-3::])