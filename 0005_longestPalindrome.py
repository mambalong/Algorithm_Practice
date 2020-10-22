'''
5. Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
动态规划，dp[i][j] 的值代表 s[i: j+1] 是否是回文字符串，对于一个长度大于二的子串，
它是不是回文的取决于两点，1. 两头的字母是否相等 2. 把两头去掉后，剩下的是不是回文。
状态转移方程 dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
边界问题，长度为 1 的子串一定是回文的，长度为二的子串只有两个元素相同的时候是回文的。
还有 i 不能小于 j
要特别注意遍历 dp 矩阵的顺序，因为长度较长的是由长度较短的结果得到的，而且我们不需要管
i > j 的情况

'''
def longestPalindrome(s):
    n = len(s)
    if n == 0:
        return 0
    dp = [[False] * n for _ in range(n)]
    res = ""

    for c in range(n):
        for r in range(c + 1):
            if r == c:
                dp[r][c] = True
            elif r + 1 == c:
                dp[r][c] = s[r] == s[c]
            else:
                dp[r][c] = dp[r+1][c-1] and s[r] == s[c]
            if dp[r][c] and c - r + 1 > len(res):
                res = s[r: c+1]
    return res

print(longestPalindrome('aacabdkacaa'))
