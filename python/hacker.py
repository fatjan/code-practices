str_len = int(input())
string = input()
word = string
def countCond(kata):
    cond = False
    cond1 = kata.count('h')
    cond2 = kata.count('a')
    cond3 = kata.count('c')
    cond4 = kata.count('k')
    cond5 = kata.count('e')
    cond6 = kata.count('r')
    cond7 = kata.count('t')
    if cond1 >= 2 and cond2 >= 2 and cond3 >= 2 and cond4 >= 1 and cond5 >= 1 and cond6 >= 2 and cond7 >= 2 and cond8 >= 1:
        cond = True
    return cond
nums = [2,2,2,1,1,2,2,1]
char = ['h','a','c','k','e','r','t']
total = 0
temp = word
while len(word) >= 11:
    print(countCond(word))
    if countCond(word):
        total += 1
        for i in range(len(nums)):
            for _ in range(nums[i]):
                temp.replace(char[i],'')
        word = temp
    else:
        break
print(total)