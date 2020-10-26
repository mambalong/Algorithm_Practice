'''
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''

'''
思路：
stack 栈，遍历 s，遇到左括号的时候，就入栈，遇到右括号的时候，判断栈顶的元素是不是对应的做括号，不是就返回 False，
是的话就是符合的，栈顶元素出栈。最后判断栈是不是空，空了，就代表 True，不空就 False
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i in pairs:
                if not stack or stack.pop() != pairs[i]:
                    return False
            else:
                stack.append(i)
        return False if stack else True
