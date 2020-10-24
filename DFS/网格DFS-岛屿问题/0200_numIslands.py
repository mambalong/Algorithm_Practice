'''
200. Number of Islands
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

'''

'''
套用岛屿问题的框架，进行了多少次 dfs 搜索，就代表有几个岛屿。
'''
class Solution:
    def inArea(self, grid, r, c):
        return 0 <= r < len(grid) and 0 <= c < len(grid[0])

    def dfs(self, grid, r, c):
        if not self.inArea(grid, r, c):
            return
        
        elif grid[r][c] != '1':
            return
        
        elif grid[r][c] == '1':
            grid[r][c] = '2'

            self.dfs(grid, r-1, c)
            self.dfs(grid, r+1, c)
            self.dfs(grid, r, c-1)
            self.dfs(grid, r, c+1)

            return
        

    def numIslands(self, grid):
        res = 0
        if len(grid) == 0: return
        nr, nc = len(grid), len(grid[0])

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    self.dfs(grid, r, c)
                    res += 1
        return res

solution = Solution()
print(solution.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
    
