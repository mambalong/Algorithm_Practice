'''

679. 24 Game
You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

Example 1:
Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24
Example 2:
Input: [1, 2, 1, 2]
Output: False
Note:
The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.
'''


'''
思路：回朔法
从四个数中取两个数，选择一种运算符号，计算的结果在放回数组代替之前那两个数。一次类推，知道数组中只剩下一个数。
就可以判断了

但是注意，因为除法的存在，判断的精度是 1e-6
除法的除数不能等于 0

'''

class Solution:
    def judgePoint24(self, nums) :
        
        def solve(nums):
            if len(nums) == 0:
                return False
            if len(nums) == 1:
                return abs(nums[0] - 24) <= 1e-6
            
            for i, x in enumerate(nums):
                for j, y in enumerate(nums):
                    # x, y 就是两个被选中的数
                    if i == j:
                        continue
                    # 创建新的数组，把为选中的数添加进去
                    new_nums = []
                    for m, n in enumerate(nums):
                        if m == i or m == j:
                            continue
                        new_nums.append(n)

                    for k in range(4):
                        # 优化，因为 + * 遵循交换律
                        if k < 2 and j > i:
                            continue
                        if k == 0:
                            new_nums.append(x + y)
                        elif k == 1:
                            new_nums.append(x * y)
                        if k == 2:
                            new_nums.append(x - y)
                        if k == 3:
                            # 除数不可以是 0
                            if abs(y - 0) <= 1e-6:
                                continue
                            new_nums.append(x / y)

                        if solve(new_nums):
                            return True
                        new_nums.pop()
            return False
        
        return solve(nums)

                    