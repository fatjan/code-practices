# Write your code here
# s_len = int(input())
# string = input()
# sort_str = sorted(string) 
# first = sort_str[-1]
# print(string[string.index(first):])

def find_strong(string):
    collections = []
    subs = ''
    for i in range(len(string)):
        subs += string[i:]
        collections.append(subs)
        subs = ''
    new_coll = sorted(collections)
    print(new_coll[-1])
find_strong('kumnlpowsa')
find_strong('ploeikxneq')
