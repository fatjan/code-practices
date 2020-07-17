T = int(input()) # number of test cases 

for _ in range(T):
    line = input()
    l1 = [int(x) for x in line.split(" ")]
    N = l1[1]
    line2 = input()
    num = [int(x) for x in line2.split(" ")]
    N = len(num)
    total = 0
    for i in range(1,N):
        while num[i] < num[i-1] or num[i] == num[i-1]:
            num[i] += N
            total += 1
    print(total)