def jumpingOnClouds(c):
    step = 0
    i = 0
    while i <= len(c)-2:
        print('i sekarang', i)
        if i+2 < len(c) - 2:
            if c[i + 2] == 0:
                print('ini loncat 2')
                step += 1
                i += 2
                print('i after jumps 2', i)
        if c[i + 1] == 0:
            step += 1
            i = i + 1
            print('ini loncat 1')
            print('i after jumps 1', i)
    return ('ini return ' + str(step))
            

# print(jumpingOnClouds([0, 0, 0, 0, 1, 0]))
# print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))
print(jumpingOnClouds([0, 0, 0, 1, 0, 0]))
# jumpingOnClouds([0, 0, 0, 0, 1, 0])
