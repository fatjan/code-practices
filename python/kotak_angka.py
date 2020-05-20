# Write your code here
cases = int(input())
result = []
inside = []
for _ in range(cases):
    num = int(input())
    out = []
    for i in range(num):
        for j in range(num):
            inside.append(i ^ j)
        out.append(inside)
        inside = []
    result.append(out)
for i in range(len(result)):
    total = 0
    max_v = max(result[i][-1])
    for j in range(len(result[i])):
        if max_v in result[i][j]:
            total += 1
    print(max_v, total)
