'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
Example 4:

Input: coins = [1], amount = 1
Output: 1
Example 5:

Input: coins = [1], amount = 2
Output: 2
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 231 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


def coinChange(coins, amount):

    memo = {}

    # Enter a target amount n, and return the minimum number of coins
    # that make up the amount.
    def dp(n, memo):

        if n in memo:
            return memo[n]

        # base case
        if n == 0:
            return 0
        if n < 0:
            return -1
        res = float('inf')
        for coin in coins:
            sub_problem = dp(n-coin)
            # no solution for sub problem, continue
            if sub_problem == -1:
                continue
            res = min(res, 1 + sub_problem)
        return res if res != float('inf') else -1
    
    return dp(amount)

def coinChange(coins, amount):
    dp = [float('inf')] * (amount+1)
            dp[0] = 0
            for i in range(0, amount+1):
                for coin in coins:
                    if i - coin < 0:
                        continue
                    dp[i] = min(dp[i], 1+dp[i-coin])
            return dp[amount] if dp[amount] != float('inf') else -1



