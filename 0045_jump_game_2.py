'''
45. Jump Game II
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''


def jump(nums):
    n = len(nums)
    jumps = 0
    farthest = 0
    end = 0

    for i in range(n-1):
        farthest = max(farthest, i + nums[i])
        if end == i:
            jumps += 1
            end = farthest
    return jumps

print(jump([2,3,1,1,4]))