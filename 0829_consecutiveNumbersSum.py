'''
829. Consecutive Numbers Sum
Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

Example 1:

Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3
Example 2:

Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
Note: 1 <= N <= 10 ^ 9.
'''

'''
思路：
一次检查是否存在 1，2，3，4 ... 个解
1 个数的解，一定存在，就是 N 本身，N - 0 除以 2 如果能整除，则有解
2 个数的解，第一个数和第二个数相差 1，N - 1 除以 2 如果能整除，则有解
3 个数的解，第一个数和第二个数相差 1， 第一个数和第三个数相差 2，N - 1 - 2 除以 3 如果能整除，则有解
依次类推
'''

class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        res, k = 0, 1
        while N > 0:
            res += N % k == 0
            N -= k
            k += 1
        return res