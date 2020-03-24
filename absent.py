def present(s):
    count_A = 0
    count_L = 0
    cond = True
    for i in s:
        if i == 'A':
            count_A += 1
            if count_A > 1:
                cond = False
                break
        elif i == 'L':
            count_L += 1
            if count_L == 3:
                cond = False
                break
        else:
            count_L = 0

    return cond


print(present("PPALLP"))
# "LALL"
print(present("LALLLP"))
