def kWeakestRows(mat, k):
        totals = []
        for i in range(len(mat)):
            totals.append(mat[i].count(1))
        print(totals)
        result = []
        for i in range(k):
            result.append(totals.index(min(totals)))
            totals[totals.index(min(totals))] = 100 ^ 2
        return result


print(kWeakestRows([[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [
      1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]], 3))
