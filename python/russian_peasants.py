def russian(a,b):
    x = a
    y = b
    z = 0
    while x > 0:
        # print(x,y,z)
        if x % 2 == 1:
            z += y
        y = y << 1
        x = x >> 1
    return z

# print(russian(17,1))
# print(russian(20,7))

import time
start_time = time.time()
russian(2**40,2**40)
print("--- %s seconds ---" % (time.time() - start_time))
