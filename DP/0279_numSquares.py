'''

279. Perfect Squares
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) 
which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

'''

'''
思路：
可以暴力枚举，需要用到递归
动态规划
dp[i] 代表 i 包含的最少的完全平方数的个数
dp 数组初始化，dp[0] = 0
后面的先初始化对应的下标的值，代表最多的情况，就是全部都是由 1 组成
状态转移方程：
dp[i] = min(dp[i], dp[i - square] + 1)
square < i

'''

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [x for x in range(n + 1)]

        for i in range(1, n+1):
            j = 1
            while i >= j * j:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        
        return dp[-1]