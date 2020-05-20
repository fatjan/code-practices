a = '12345628290'
b = '1'
c = '3'
cond = False
for i in range(len(a)-1):
    sub = a[i:i+2]
    print(sub)
    if b in sub and c in sub:
        cond = True
print(cond)
