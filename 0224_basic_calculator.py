'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, 
non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.

'''



def calculate(s):
    
    def eveluate_expr(stack):
        res = stack.pop() if stack else 0
        while stack and stack[-1] != ')':
            sign = stack.pop()
            if sign == '+':
                res += stack.pop()
            elif sign == '-':
                res -= stack.pop()
        return res
    
    stack = []
    pv, operand = 0, 0

    for i in range(len(s)-1, -1, -1):
        cha = s[i]
        
        if cha.isdigit():
            operand += 10 ** pv * int(cha)
            pv += 1
        
        elif cha != ' ':
            if pv:
                stack.append(operand)
                pv, operand = 0, 0
            if cha == '(':
                res = eveluate_expr(stack)
                stack.pop()
                stack.append(res)
            else:
                stack.append(cha)

    if pv:
        stack.append(operand)   

    return eveluate_expr(stack)

print(calculate('2+(3+4)-4'))
