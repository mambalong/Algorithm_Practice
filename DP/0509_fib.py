'''

509. Fibonacci Number
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

 

Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

Note:

0 ≤ N ≤ 30.
'''

# 最基础的递归
class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1
        return self.fib(N-1) + self.fib(N-2)

# 带有备忘录的递归，上面的算法低效的原因主要是重复计算子问题
class Solution:
    def helper(self, n, memo):
        # 如果已经计算过
        if n in memo:
            return memo[n]
        else:
            # base case
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                # 递归，这里需要更新备忘录
                memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
                return memo[n]

    def fib(self, N: int) -> int:
        memo = {}
        return self.helper(N, memo)

# 动态规划，就是自底向上的解法
class Solution:
    def fib(self, N: int) -> int:
        dp = [0 for _ in range(N+1)]
        # 判断一下 N 是否大于等于 1，否则，就不需要进行下一步了
        if N >= 1:
            dp[1] = 1
        for i in range(2, N+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[N]

# 动态规划的状态压缩
class Solution:
    def fib(self, N: int) -> int:
        if N == 0:  return 0
        if N == 1:  return 1
        pre, curr = 0, 1
        for i in range(2, N + 1):
            summ = pre + curr
            pre, curr = curr, summ
        return curr
