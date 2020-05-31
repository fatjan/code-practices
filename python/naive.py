def naive(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        if x == 20:
            print(z)
        z = z + y
        x = x - 1
    return z

print(naive(63,12))

# import time
# start_time = time.time()
# naive(2**40,2**40)
# print("--- %s seconds ---" % (time.time() - start_time))