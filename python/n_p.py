# test_num = int(input())
# n = []
# p = []
# for test in range(test_num):
#     line = input()
#     n.append(int(line[0]))
#     p.append(int(line[2]))
# print(n, p)
# sub = 'Y'
# coll = []
# j = 0
# while j < 2**(n[1]-1):
#     for i in range(1,n[1]):
#         if i % 2:
#             sub += 'X'
#         else:
#             sub += 'Y'
#     coll.append(sub)  
#     sub = 'Y'
#     j += 1
# print(coll)
# coll = list(set(coll))
# print(coll)
a = []
def permutations(string, step = 0):
    if step == len(string):
        # we've gotten to the end, print the permutation
        a.append(''.join(string))
    for i in range(step, len(string)):
        # copy the string (store as array)
        string_copy = [c for c in string]
         # swap the current index with the step
        string_copy[step], string_copy[i] =string_copy[i], string_copy[step]
         # recurse on the portion of the stringthat has not been swapped yet
        permutations(string_copy, step + 1)
permutations ('YXXX')
print(a)
print(len(a))