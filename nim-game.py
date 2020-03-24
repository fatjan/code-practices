def canWinNim(n):
        s = n
        if n <= 3:
            return True
        else:
            for i in range(1, 4):
                if i == 1:
                    me = 1
                    opp = 4-me
                    s = me-opp
