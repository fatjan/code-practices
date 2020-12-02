def foo(num, a, b, i, j):
    k = j
    ct = 0
    while k > i - 1:
        if num[k] <= b and num[k] > a:
            ct += 1
        k -= 1
    return ct

x = [11,10,10,5,10,15,20,10,7,11]

print(foo(x,9,16,3,6))
print(foo(x,10,20,0,4))
print(foo(x,9,16,6,3))
print(foo(x,20,10,0,4))
print(foo(x,6,7,8,8))