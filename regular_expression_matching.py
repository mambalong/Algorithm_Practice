# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# Note:

# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like . or *.
# Example 1:

# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:

# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# Example 4:

# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
# Example 5:

# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false

# This version did not pass. I did not find the problem.
# def isMatch(s, p):
#     if s == None or p == None:
#         return False

#     sLen, pLen = len(s), len(p)

#     dp = [[False]*(pLen+1) for _ in range(sLen+1)]
#     # base case
#     dp[0][0] = True
#     for j in range(1, pLen+1):
#         if p[j-1] == '*':
#             dp[0][j] == dp[0][j-2]
    
#     # dp
#     for i in range(1, sLen+1):
#         for j in range(1, pLen+1):
#             # s[i-1] and p[j-1] matches
#             if s[i-1] == p[j-1] or p[j-1] == '.':
#                 dp[i][j] = dp[i-1][j-1]
#             # s[i-2] and p[j-1] don't match
#             else:
#                 # p[j-1] is '*'
#                 if p[j-1] == '*':
#                     # s[i-1] and p[j-2] matches
#                     if s[i-1] == p[j-2] or p[j-2] == '.':
#                         dp[i][j] = dp[i][j-2] or dp[i-1][j-2] or dp[i-1][j]
#                     # s[i-1] and p[j-2] dont match
#                     else:
#                         dp[i][j] = dp[i][j-2]
    
#     return dp[-1][-1]


def isMatch(s, p):
    if s == None and p == None:
        return True
    
    sLen, pLen = len(s), len(p)
    dp = [[False] * (pLen + 1) for _ in range(sLen+1)]
    # base case
    dp[0][0] = True
    for j in range(1, pLen+1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-2]

    def matches(i, j):
        print(i, j)
        if p[j] == '.':
            return True
        return s[i] == p[j]
    
    for i in range(1, sLen+1):
        for j in range(1, pLen+1):
            if p[j-1] != '*':
                if matches(i-1, j-1):
                    dp[i][j] = dp[i-1][j-1]

            else:
                if matches(i-1, j-2):
                    dp[i][j] = dp[i][j-2] or dp[i-1][j] or dp[i-1][j-2]
                else:
                    dp[i][j] = dp[i][j-2]
    
    return dp[sLen][pLen]

print(isMatch("aab", "c*a*b"))


