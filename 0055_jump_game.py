'''
55. Jump Game
Given an array of non-negative integers, you are initially positioned at the
 first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum 
jump length is 0, which makes it impossible to reach the last index.
'''

'''
贪心
对于每一个位置，我们算出从这个位置之前的所有位置起跳能到达的最远的地方，
如果这个最远距离小于或等于 i，当前索引，那么就证明它已经没办法跳到下一个了，
就是False

最后遍历完成的后，判断最远距离是不是大于数组的长度。
注意我们只需要遍历 n-1 元素，因为我们要的是能不能跳到最后一个索引
而且我们的设定是，判断能不能从 0 到 当前索引这个区间内的格子跳出去。
'''
class Solution:
    def canJump(self, nums) -> bool:
        n = len(nums)
        farthest = 0

        for i in range(n-1):
            farthest = max(farthest, i + nums[i])
            if farthest <= i:
                return False
        return farthest >= n-1