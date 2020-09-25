# 链接：https://www.nowcoder.com/questionTerminal/af3ce410dd694983a01034141eafa0a4
# 来源：牛客网

# 任务务调度在分布式调度系统中是一个很复杂很有挑战的问题。这里我们考虑一个简化的场景：假设一个中央调度机，
# 有n个相同的任务需要调度到m台服务器上去执行。由于每台服务器的配置不一样，因此服务器执行一个任务所花费的时
# 间也不同。现在假设第i个服务器执行一个任务需要的时间为t[i]。

# 例如：有2个执行机a, b. 执行一个任务分别需要7min，10min，有6个任务待调度。如果平分这6个任务，即a，b
# 各分三个任务，则最短需要30min执行完所有。如果a分这4个任务，b分2个，则最短28min执行完。

# 请设计调度算法，使得所有任务完成所需的时间最短

# 1) 简述思路
# 2) 请用你熟悉的编程语言编码实现以下方法，输入为m台服务器，每台机器处理一个任务的时间为t[i]，完成n个任务，
# 输出n个任务在m台服务器的分布：

# (1) 思路：记录每一个服务器已经累计执行的时间，对于一个新任务，选取的对应服务器需符合一下条件，已累计执行时间加上新任务
# 耗时要最小。

t = [7, 8, 10]
m = len(t)
n = int(input())

def estimate_process_time(t, m, n):
    cost = [0] * m
    for i in range(n):
        chosen = 0
        lst = cost[chosen] + t[chosen]
        for j in range(m):
            tmp = cost[j] + t[j]
            if tmp < lst:
                chosen = j
                lst = tmp
        cost[chosen] = lst
    print(cost)
    print(max(cost))

estimate_process_time(t, m, n)


