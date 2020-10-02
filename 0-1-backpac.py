# 给你一个可装载重量为W的背包和N个物品，每个物品有重量和价值两个属性。
# 其中第i个物品的重量为wt[i]，价值为val[i]，现在让你用这个背包装物品，
# 最多能装的价值是多少？

def backpack(N, W, wt, val):
    # for the first i itmes, the capacity of the backpack is w.
    # the maximum value that can be loaded is dp[i][w]
    dp = [[0] * (N+1) for _ in range(W+1)]
    for i in range(1, N+1):
        for w in range(1, W+1):
            # if we cannot put the ith item in the pack
            if wt[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                # put or not put in to the pack, choose the best one
                dp = max(dp[i-1][w], dp[i - 1][w - wt[i-1]] + val[i-1])
    return dp[N][W]
