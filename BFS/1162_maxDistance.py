
from collections import deque

def neighbours(grid, i, j):
    res = []
    n = len(grid)
    for d in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        a = i + d[0]
        b = j + d[1]
        if 0 <= a < n and 0 <= b < n:
            res.append((a, b))
    return res

def maxDistance(grid):
    def bfs(grid, m, n):
        que = deque([(m, n)])
        seen = set([(m, n)])
        dis = 0
        
        while que:
            sz = len(que)
            for i in range(sz):
                cur= que.popleft()
                if grid[cur[0]][cur[1]] == 1:
                    return dis
                for nei in neighbours(grid, cur[0], cur[1]):
                    if nei not in seen:
                        que.append(nei)
                        seen.add(nei)
            dis += 1
        return -1
    
    res = -1
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 1:
                # res.append(-1)
                continue
            res = max(res, bfs(grid, i, j))
    
    return res

print(maxDistance([[1,1,0,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]))



