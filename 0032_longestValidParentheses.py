'''
32. Longest Valid Parentheses
Given a string containing just the characters '(' and ')', find the length of the 
longest valid (well-formed) parentheses substring.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
'''

'''
栈
我们需要栈底元素为已经遍历过的元素中，最后一个未被匹配的右括号的下标，栈内其他的元素用于维护做括号的下标。
对于每个遇到的左括号，我们把它的下标入栈。
对于每个遇到的右括号，我们先将栈顶元素 pop，代表匹配了当前右括号
如果栈为空，将右括号入栈
如果栈不为空，则更新答案

注意，栈的初始状态有一个 -1，是为了满足，栈底元素为已经遍历过的元素中，最后一个未被匹配的右括号的下标，
这个设定。
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])
        
        return ans
