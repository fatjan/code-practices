def rec_russian(a,b):
    if a == 0:
        return 0
    if a % 2 == 0:
        return 2 * rec_russian(a/2, b)
    return b + 2 * rec_russian((a-1)/2, b)

# print(rec_russian(3,4))

import time
start_time = time.time()
rec_russian(2**40,2**40)
print("--- %s seconds ---" % (time.time() - start_time))


  