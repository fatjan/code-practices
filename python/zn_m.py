test_cases = int(input())
for _ in range(test_cases):
    line = input()
    line_list = line.split(' ')
    length = int(line_list[0])
    line2 = input()
    line2_list = line2.split(' ')
    not1 = line2_list[0]
    not2 = line2_list[1]
    div = int(line_list[1])
    limit = 10 ** length
    nums = []
    for i in range(1,limit):
        if limit == 10 and i % div == 0:
                nums.append(i)
        elif i % div == 0:
            num = str(i)
            for j in range(len(num)):
                if not1 not in num[j:j+2] and not2 not in num[j:j+2]:
                    nums.append(i)
    print(len(nums))