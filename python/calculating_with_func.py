def zero(num): return 0
def one(num): return 1
def two(): return 2
def three(): return 3
def four(num): return 4
def five(): return 5
def six(num): return 6
def seven(num):return 7
def eight(num): return 8
def nine(): return 9

def plus(num): return + num
def minus(num): return - num
def times(num): return num
def divided_by(num): return num

print(seven(times(five()))) # must return 35
print(four(plus(nine()))) # must return 13
print(eight(minus(three()))) # must return 5
print(six(divided_by(two()))) # must return 3