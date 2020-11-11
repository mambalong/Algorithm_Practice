'''
72. Edit Distance
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
'''

'''
思路：动态规划
dp[i][j] 表示将 word1 的前 i 个字符转换成 word2 的前 j 个字符所需要的最小步数
状态转移方程：
两种情况：
1. 当 word1[i] == word[j]
    dp[i][j] = dp[i-1][j-1]
2. 当 word1[i] ！= word[j]
    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    上面 min 里面分别代表了替换，删除，插入操作

base case:
当两个 word 任意一个为空的时候，我们是知道结果的
例如当 word1 为空的时候，就是 dp table 的第一行，我们只需要连需进行插入操作
当 word2 为空的时候，就是 dp table 的第一列，我们只需要连需进行删除操作
两个都是空的话，就不需要操作
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        # base case
        for i in range(n1 + 1):
            dp[i][0] = i
        for j in range(n2 + 1):
            dp[0][j] = j

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        
        return dp[n1][n2]