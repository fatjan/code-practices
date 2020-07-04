line = input()
l1 = [int(x) for x in line.split(" ")]
n = l1[0]
m = l1[1]
k = l1[2]
total = 0
isi_arr = []
for _ in range(n):
    new_line = input()
    l1 = [int(x) for x in new_line.split(" ")]
    isi_arr.append(l1)

total_f = 0

for i in range(n):
    for j in range(1, isi_arr[i][-1] + 1):
        if i == j:
            a = isi_arr[i][0]
            b =isi_arr[i][1]
            # print(a,b,j)
            f_i_j = isi_arr[i][0] * j * j + isi_arr[i][1]
            total_f += f_i_j
if total_f % k == 0:
    total += 1
total_f = 0
print('total ', total)