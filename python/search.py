words = 'apple lettuce limes avocado'
cases = int(input())

def search_engine(kata):
    w_arr = words.split(' ')
    if kata in w_arr:
        return True
    return False

for _ in range(cases):
    word = input()
    print(search_engine(word))
