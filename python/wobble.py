'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def check_wobble(num):
    a = num[0]
    b = num[1]
    cond = True
    if a == b:
        return False
    for i in range(len(num)):
        if i % 2 == 0 and num[i] == a or i % 2 != 0 and num[i] == b:
            continue
        else:
            cond = False
            break
    return cond

tcases = int(input())
for _ in range(tcases):
    line = input()
    line = line.split(' ')
    n = int(line[0])
    kth = int(line[1])
    k = 0
    num = ''
    nums = []
    while k < kth:
        for i in range(1,n):
            for j in range(1,10):
                if j % 2 != 0: 
                    num += str(j)
                else:
                    num += str(i)
            print(num)
            if len(num) == n:
                if check_wobble(num):
                    nums.append(num)
                num = ''
                k += 1
                break
    if len(nums) == kth:
        print(nums[-1])
    else:
        print(1)

