'''
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-greater-element-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = list(reversed(nums))

        for i in range(n-1, -1, -1):
            while stack and nums[i] >= stack[-1]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(nums[i])
        return res