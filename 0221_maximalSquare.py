'''

221. Maximal Square
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4

'''

'''
思路动态规划，dp[i][j] 表示以当前格子为右下角，最大的正方形的边长。
dp 方程：dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
base case:
当 i 或者 j 等于 0 时，dp 值等于对应格子的值。

'''

class Solution:
    def maximalSquare(self, matrix):
        if matrix == []:
            return 0
        max_side = 0
        nr, nc = len(matrix), len(matrix[0])
        dp = [[0] * nc for _ in range(nr)]

        for i in range(nr):
            for j in range(nc):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_side = max(max_side, dp[i][j])
        return max_side * max_side

