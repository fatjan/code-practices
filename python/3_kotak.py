# Write your code here
cases = int(input())
result = []
inside = []
for _ in range(cases):
    num = int(input())
    out = []
    amount = 0
    if num == 2:
        max_v = num-1
    else:
        max_v = num
    for i in range(num):
        for j in range(num):
            inside.append(i ^ j)
        amount += inside.count(max_v)
        inside = []
    print(max_v,amount)
# print(result)
# for i in range(len(result)):
#     total = 0
#     max_v = max(result[i][-1])
#     for j in range(len(result[i])):
#         if max_v in result[i][j]:
#             total += 1
#     print(max_v, total)
