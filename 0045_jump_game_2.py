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

'''
思路：贪心
以 [2,3,1,1,4] 为例子，初始状态，我们在位置 0 处，我们最远可以跳到位置 2 处，在 0-2 这个区域内，
我们从位置 1 处可以跳出这个区域，并跳的最远，所以我们第一步就从位置 0 跳到位置 1，后面的依次类推。

根据上面的描述，你可能认为会出现重复遍历数组的情况，但是其实我们只需要遍历一次数组即可，只需要在合适
的时机更新最远能跳到的距离，区域的边界，步数即可。

'''
class Solution:
    def jump(self, nums) -> int:
        n = len(nums)
        farthest, end, step = 0, 0, 0

        for curr in range(n-1):
            if farthest >= curr:
                # 从 0 到当前位置这个区域内能跳到的最远位置
                farthest = max(farthest, curr + nums[curr])
                # 当到达边界的时候，我们在更新边界，并且步数加一
                if end == curr:
                    end = farthest
                    step += 1
        
        # 返回记过的时候判断一下，如果边界小于 n-1 就代表不可能跳到最后一个元素
        return step if end >= n - 1 else -1

solution = Solution()
print(solution.jump([2,3,1,1,1,0,0]))


