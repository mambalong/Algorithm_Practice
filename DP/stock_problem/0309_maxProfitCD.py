'''
309. Best Time to Buy and Sell Stock with Cooldown
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
'''

'''
只需要把 cd 引入到状态转移方程就好了
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i-1])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-2][k][0] - prices[i-1])
在第 i 天选择买入的时候，要从 i-2 进行状态转移。
'''

class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = -float('inf')
        dp_pre_0 = 0

        for i in range(1, n+1):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i-1])
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i-1])
            dp_pre_0 = tmp
        
        return dp_i_0