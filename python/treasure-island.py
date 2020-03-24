def treasureIsland(arr_map):
    # find the location of treasure
    for i in range(len(arr_map)):
        for j in range(len(arr_map)):
            if arr_map[i][j] == 'X':
                tre_loc = [i,j]
    
    # start to find the route to the treasure location
    # check right and bottom to see safe route
    route = [[0,0]]
    for i in range(len(arr_map)):
        for j in range(len(arr_map)):
            if i == 0 and j < len(arr_map)-1:
                # check right side
                if checkSafe(arr_map[i][j+1]) and [i, j+1] not in route:
                    route.append([i,j+1])
                # check bottom side
                if checkSafe(arr_map[i + 1][j]) and [i+1, j] not in route:
                    route.append([i + 1, j])
            elif i == 0 and j == len(arr_map)-1:
                # check bottom side
                if checkSafe(arr_map[i + 1][j]) and [i+1, j] not in route:
                    route.append([i + 1, j])
            elif i > 0 and i < len(arr_map) - 1:
                if j == 0:
                    # check right side
                    if checkSafe(arr_map[i][j+1]) and [i, j+1] not in route:
                        route.append([i, j+1])
                    # check bottom side
                    if checkSafe(arr_map[i + 1][j]) and [i+1, j] not in route:
                        route.append([i + 1, j])
                elif j == len(arr_map) - 1:
                    # check left side
                    if checkSafe(arr_map[i][j-1]) and [i, j-1] not in route:
                        route.append([i, j-1])
                    # check bottom side
                    if checkSafe(arr_map[i + 1][j]) and [i+1, j] not in route:
                        route.append([i + 1, j])
                else:
                    # check right side
                    if checkSafe(arr_map[i][j+1]) and [i, j+1] not in route:
                        route.append([i, j+1])
                    # check left side
                    if checkSafe(arr_map[i][j-1]) and [i, j-1] not in route:
                        route.append([i, j-1])
                    # check bottom side
                    if checkSafe(arr_map[i + 1][j]) and [i+1, j] not in route:
                        route.append([i + 1, j])
            else:
                if j == 0:
                    # check right side
                    if checkSafe(arr_map[i][j+1]) and [i, j+1] not in route:
                        route.append([i, j + 1])
                elif j == len(arr_map) - 1:
                    # check left side
                    if checkSafe(arr_map[i][j-1]) and [i, j-1] not in route:
                        route.append([i, j - 1])
                else:
                    # check right side
                    if checkSafe(arr_map[i][j+1]) and [i, j+1] not in route:
                        route.append([i, j + 1])
                    # check left side
                    if checkSafe(arr_map[i][j-1]) and [i, j-1] not in route:
                        route.append([i, j - 1])
                    

    print(route) 
                    

def checkSafe(cond):
    if cond == 'O':
        return True
    else:
        return False


treasureIsland([
    ['O', 'O', 'O', 'O'],
    ['D', 'O', 'D', 'O'],
    ['O', 'O', 'O', 'O'],
    ['X', 'D', 'D', 'O'],
])
