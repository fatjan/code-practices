def get_adj(num):
    grid = []
    grid.append(['1','2','3'])
    grid.append(['4','5','6'])
    grid.append(['7','8','9'])
    grid.append(['','0',''])
    adj = []
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == num:
                adj.append(val)
                if i == 0:
                    if j == 0:
                        adj.append(grid[i][j+1])
                        adj.append(grid[i+1][j])
                    if j == 1:
                        adj.append(grid[i][j-1])
                        adj.append(grid[i+1][j])
                        adj.append(grid[i][j+1])
                    if j == 2:
                        adj.append(grid[i][j-1])
                        adj.append(grid[i+1][j])
                if i == 1:
                    if j == 0:
                        adj.append(grid[i-1][j])
                        adj.append(grid[i][j+1])
                        adj.append(grid[i+1][j])
                    if j == 1:
                        adj.append(grid[i-1][j])
                        adj.append(grid[i][j-1])
                        adj.append(grid[i+1][j])
                        adj.append(grid[i][j+1])
                    if j == 2:
                        adj.append(grid[i-1][j])
                        adj.append(grid[i][j-1])
                        adj.append(grid[i+1][j])
                if i == 2:
                    if j == 0:
                        adj.append(grid[i][j+1])
                        adj.append(grid[i-1][j])
                    if j == 1:
                        adj.append(grid[i][j-1])
                        adj.append(grid[i+1][j])
                        adj.append(grid[i][j+1])
                        adj.append(grid[i-1][j])
                    if j == 2:
                        adj.append(grid[i][j-1])
                        adj.append(grid[i-1][j])
                if i == 3:
                        adj.append(grid[i-1][j])
    return adj

def get_pins(observed):
    adjs = []
    for i in range(len(observed)):
        adjs.append(get_adj(observed[i]))   
   
    import itertools

    if len(adjs) == 1:
        return adjs
    elif len(adjs) == 2:
        hasil = [''.join(i) for i in itertools.product(adjs[0], adjs[1])]
        return hasil
    else:
        hasil = [''.join(i) for i in itertools.product(adjs[0], adjs[1])]
        for i in range(2,len(adjs)):
            hasil = [''.join(i) for i in itertools.product(hasil, adjs[i])]
        return hasil

print(get_pins('8'))
print(get_pins('16'))
print(get_pins('129'))