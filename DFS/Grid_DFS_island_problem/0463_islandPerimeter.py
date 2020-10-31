'''
463. Island Perimeter
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 
represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by 
water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. 
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. 
Determine the perimeter of the island.

 

Example 1:


Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4
'''

class Solution:
    
    def inArea(self, grid, r, c):
        return 0 <= r < len(grid) and 0 <= c < len(grid[0])

    def dfs(self, grid, r, c):
        if not self.inArea(grid, r, c):
            return 1
        elif grid[r][c] == 0:
            return 1
        elif grid[r][c] == 2:
            return 0
        elif grid[r][c] == 1:
            grid[r][c] = 2

            return self.dfs(grid, r-1, c) + self.dfs(grid, r+1, c) + self.dfs(grid, r, c-1) + self.dfs(grid, r, c+1)


    def islandPerimeter(self, grid):
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return self.dfs(grid, r, c)
        return 0
    
solution = Solution()
print(solution.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
print(solution.islandPerimeter([[1,1]]))