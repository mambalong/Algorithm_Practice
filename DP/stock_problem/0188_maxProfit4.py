'''

188. Best Time to Buy and Sell Stock IV
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Notice that you may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
 

Constraints:

0 <= k <= 109
0 <= prices.length <= 1000
0 <= prices[i] <= 1000
'''

'''
直接套用 k = 2 的解法
'''

class Solution:
    def maxProfit(self, k: int, prices):
        n = len(prices)
        dp = [[[0] * 2 for _ in range(k+1)] for _ in range(n+1)]

        for i in range(n+1):
            for kk in range(k+1):
                # base case
                if i == 0:
                    dp[i][kk][1] = -float('inf')
                    continue
                if kk == 0:
                    dp[i][kk][1] = -float('inf')
                    continue
                
                dp[i][kk][0] = max(dp[i-1][kk][0], dp[i-1][kk][1] + prices[i-1])
                dp[i][kk][1] = max(dp[i-1][kk][1], dp[i-1][kk-1][0] - prices[i-1])

        return dp[n][k][0] if dp[n][k][0] != -float('inf') else -1