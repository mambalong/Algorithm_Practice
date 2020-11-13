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


# 暴力递归算法
class Solution:
    def coinChange(self, coins, amount):
        # base case
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        
        # 将 res 初始为无穷大，因为是要求最小的
        res = float('inf')
        for coin in coins:
            sub_problem = self.coinChange(coins, amount - coin)
            # 如果子问题不成立，则跳过
            if sub_problem == -1:
                continue
            res = min(res, sub_problem + 1)

        # 输出结果的时候一定要判断 res 是不是还是无穷大
        return res if res != float('inf') else -1

# 备忘录优化递归算法
class Solution:
    def helper(self, coins, amount, memo):
        # 如果已经计算过
        if amount in memo:
            return memo[amount]
        else:
            # base case
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            res = float('inf')
            for coin in coins:
                sub_problem = self.helper(coins, amount - coin, memo)
                if sub_problem == -1:
                    continue
                res = min(res, 1 + sub_problem)
            
            memo[amount] = res if res != float('inf') else -1
        
        return memo[amount]
            
        
    def coinChange(self, coins, amount):
        memo = {}
        return self.helper(coins, amount, memo)

'''
动态规划
dp[i] 代表 amount 为 i 至少需要多少硬币
base case： dp[0] = 0
dp[i] = min(dp[i], dp[i - coin] + 1)
'''
class Solution:
    def coinChange(self, coins, amount):
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for i in range(1,amount + 1):
            for coin in coins:
                if i < coin:
                    continue
                dp[i] = min(dp[i], 1 + dp[i - coin])
        return dp[amount] if dp[amount] != float('inf') else -1

solution = Solution()
print(solution.coinChange([1,2,5], 11))
        