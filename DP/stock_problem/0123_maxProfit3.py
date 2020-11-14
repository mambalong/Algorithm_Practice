'''
123. Best Time to Buy and Sell Stock III
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
Example 4:

Input: prices = [1]
Output: 0

'''

class Solution:
    def maxProfit(self, prices):
        K = 2
        n = len(prices)
        dp = [[[0] * 2 for _ in range(K+1)] for _ in range(n+1)]

        for i in range(n+1):
            for k in range(K+1):
                # base case
                if i == 0:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -float('inf')
                    continue
                if k == 0:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -float('inf')
                    continue
                
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i-1])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i-1])
        
        return dp[n][K][0] if dp[n][K][0] != -float('inf') else -1