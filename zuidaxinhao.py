'''
华为机试题，给一个矩阵，里面是正整数代表网络信号，从左上角到右下角，每条路径的信号值
是那个路径上最小的数值，所有路径中最大的信号值。

'''
r = int(input())
c = int(input())
grid = []
for i in range(r):
    grid.append(list(map(int, input().split(' '))))

dp = [[0] * c for _ in range(r)]
dp[0][0] = grid[0][0]

def give_pres(m, n, r, c):
    pres = []
    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        mm = m + i
        nn = n + j
        if mm < 0 or mm == r or nn < 0 or nn == c:
            continue
        pres.append([mm, nn])
    return pres

for m in range(r):
    for n in range(c):
        if m == 0 and n == 0:
            continue
        pres = give_pres(m, n, r, c)
        max_pre = -float('inf')
        for pre in pres:
            max_pre = max(max_pre, dp[pre[0]][pre[1]])
        dp[m][n] = min(max_pre, grid[m][n])

print(dp[r-1][c-1])
