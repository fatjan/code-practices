import math
test_num = 2
cases = []
for _ in range(test_num):
    line = '8 5 8 100 90 320'
    line = line.split(' ')
    t0 = int(line[0])
    t1 = int(line[1])
    t2 = int(line[2])
    v1 = int(line[3])
    v2 = int(line[4])
    d = int(line[5])
    if t0 < t1 and t0 < t2:
        print(-1)
        continue
    T1 = d / v1 * 60
    T1 = math.ceil(T1)
    T2 = d / v2 * 60
    T2 = math.ceil(T2)
    total_t1 = t1 + T1
    total_t2 = t2 + T2
    if total_t1 < total_t2:
        print(total_t1)
    else:
        print(total_t2)

# 1
# 5 5 8 100 90 320