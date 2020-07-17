from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        q = deque()
        
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 2:
                    q.append((i, j))
        print(q)
        distance = -1 if q else 0
        
        while q:
                        
            for _ in range(len(q)):
                
                i, j = q.pop()
                
                if i > 0 and grid[i-1][j] == 1:
                    q.appendleft((i - 1, j))
                    grid[i-1][j] = 2
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    q.appendleft((i + 1, j))
                    grid[i+1][j] = 2
                if j > 0 and grid[i][j-1] == 1:
                    q.appendleft((i, j-1))
                    grid[i][j-1] = 2
                if j < len(grid[0]) - 1 and grid[i][j+1] == 1:
                    q.appendleft((i, j+1))
                    grid[i][j+1] = 2
                    
            distance += 1

        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 1:
                    return -1
        
        return distance

grid_question = [[2,1,1],[1,1,0],[0,1,1]]
# grid_question = [[2,1,1],[0,1,1],[1,0,1]]
# grid_question = [[0,2]]
answer = Solution()
result = answer.orangesRotting(grid_question)

print(result)