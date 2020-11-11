'''
166. Fraction to Recurring Decimal
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

 

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
Example 4:

Input: numerator = 4, denominator = 333
Output: "0.(012)"
Example 5:

Input: numerator = 1, denominator = 5
Output: "0.2"
'''

'''
模拟除法的过程
要注意边界条件
正负号，可以用 异或 运算来判断结果的正负号，异或运算，相同输出 0， 不同输出 1
'''

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        res = []

        # 判断结果的符号
        if (numerator < 0) ^ (denominator < 0):
            res.append('-')
        # 取绝对值
        numerator = abs(numerator)
        denominator = abs(denominator)

        quotient = numerator // denominator
        remainder = numerator % denominator
        res.append(str(quotient))

        if remainder:
            res.append('.')
            dic = {}
            while remainder != 0:
                # 出现重复的余数，说明有循环
                if remainder in dic:
                    res.insert(dic[remainder], '(')
                    res.append(')')
                    return ''.join(res)
                # 记录做括号的位置
                dic[remainder] = len(res)
                # 余数乘 10 继续除法
                numerator = remainder * 10
                quotient = numerator // denominator
                remainder = numerator % denominator
                res.append(str(quotient))
        
        return ''.join(res)





