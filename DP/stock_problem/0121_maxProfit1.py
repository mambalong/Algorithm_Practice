'''
121. Best Time to Buy and Sell Stock
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one 
share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

'''

'''
股票买卖的思路，动态规划
我们首先明确有哪几个状态，然后我们对状态进行枚举即可
状态：天数，最大交易次数，是否持有股票
我们可以用一个三维的 dp 数组来表示出所有的状态
例如 dp[i][k][0] 就表示在第 i 天，至今最多交易了 k 次，手中没有持有股票的状态下的最大盈利。

状态转移方程：
我们可以进行三种操作，买入，卖出，什么也不做，我们这里在买入的时候才更新交易次数
这里要注意第 i 天的价格是 prices[i-1]，因为他对应的 index 要减 1
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i-1])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i-1])

base case:
dp[0][k][0] = 0            第 0 天代表还没有开始，自然没有利润
dp[0][k][1] = -infinity    因为还没有开始，不可能持有股票，用负无穷表示不可能  
dp[i][0][0] = 0            k = 0 表示不允许交易，自然没有利润
dp[i][0][1] = -infinity    k = 0，所以不可能持有股票，用负无穷表示不可能

这道题 k=1，带入到状态转移方程中会发现，k 的值没有关系，可以直接忽略 k

'''

class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        dp = [[0] * 2 for _ in range(n+1)]
        dp[0][1] = -float('inf')
        for i in range(1, n+1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i-1])
            dp[i][1] = max(dp[i-1][1],  - prices[i-1])
        return dp[n][0]

class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = -float('inf')
        for i in range(1, n+1):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i-1])
            dp_i_1 = max(dp_i_1, -prices[i-1])
        return dp_i_0

solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))