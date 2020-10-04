from itertools import product
import math


def isPrime(num):
    if num < 0:
        num = -num
    if num > 2:
        for i in range(2, int(math.sqrt(num)+1)):
            if num % i == 0:
                return False
    return True

# n = int(input())
nums = list(map(int, input().split(' ')))
# odds, evens = [], []
# for i in nums:
#     if i % 2 == 0:
#         evens.append(i)
#     else:
#         odds.append(i)

# prods = list(product(odds, evens))

# prime_pairs = []
# for i in prods:
#     a, b = i[0], i[1]
#     if isPrime(a + b):
#         prime_pairs.append((a, b))

# print(prime_pairs)
# res = 0
# tmp = set()
# for i in range(len(prime_pairs)):
#     pair_i = prime_pairs[i]
#     tmp.add(pair_i[0])
#     tmp.add(pair_i[1])
#     for j in range(len(prime_pairs)):
#         pair_j = prime_pairs[j]
#         if i == j:
#             continue
#         m, n = pair_j[0], pair_j[1]
#         if not m in tmp and not n in tmp:
#             tmp.add(m)
#             tmp.add(n)
#     # print(tmp)

#     res = max(res, len(tmp))
#     tmp = set()
# print(res//2)

dp = [0] * (len(nums) + 1)
for i in range(len(nums)-2, -1, -1):
    for j in range(len(nums)-1, i, -1):
        if isPrime(nums[i] + nums[j]):
            cnt = dp[i + 1] - dp[j - 1] + dp[j + 1] + 1
        else:
            cnt = dp[i + 1]
        if cnt > dp[i]:
            dp[i] = cnt
print(dp[0])
