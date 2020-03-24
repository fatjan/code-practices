def hourglassSum(arr):
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            print(arr[i][j], end=' ')
        print()

        


hourglassSum([[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [
             0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]])
