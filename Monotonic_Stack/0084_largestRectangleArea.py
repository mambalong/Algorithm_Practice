'''
84. Largest Rectangle in Histogram
Given n non-negative integers representing the histogram's bar height 
where the width of each bar is 1, find the area of largest rectangle 
in the histogram.

'''

'''

这个题的暴力解法很容易想，我们可以枚举每一个高，然后想两侧寻找宽的边界，即找到第一个比自身高度小的高度。
但是这样时间复杂度会是 O(N2)

可以使用单调栈，分别找到每个高左右两边的边界，这样我们只需要遍历两遍 heights，负责度是 O(N)
只需要顺序遍历数组，用一个 stack，stack 如果 stack 顶部的元素比当前元素大，就 pop() 出去，
因为我们要找比当前元素小的，最后栈顶的元素就是左边最近的比当前元素小的。
在遍历过程中，每次 pop 出去的元素也有用，被 pop 出的元素，它的右边最近的比它小的元素就是当前遍历的
元素。
'''

class Solution:
    def largestRectangleArea(self, heights) -> int:
        n = len(heights)
        left, right = [-1] * n, [n] * n

        # left
        mono_stack = []
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                right[mono_stack.pop()] = i
            if mono_stack:
                left[i] = mono_stack[-1]
            mono_stack.append(i)

        print(left)
        print(right)
        res = 0
        for i, h in enumerate(heights):
            res = max(res, h * (right[i] - left[i] - 1))
        
        return res

solution = Solution()
print(solution.largestRectangleArea([2,1,5,6,2,3]))
        