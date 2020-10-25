'''
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''

# Return the index of the desired result
'''
思路很简单，在遍历数组的过程中，同时维护一个字典，字典储存的是元素的值和索引，
这样我们在找 target - x 的时候就只需要 o(1) 的时间
'''
class Solution:
    def twoSum(self, nums, target):
        dic = dict()
        for i, num in enumerate(nums):
            if target - i in dic:
                return [dic[target - num], i]
            dic[num] = i
        return []

# Return the values of two desired numbers
'''
这里对题目稍微改动一下，让我们的方法直接输出两个数各自的值，如果有多对结果，
只要不重复，我们都输出
比如 twoSum([1,2], 3) 输出 [1,2]
这样做是为了写一个可以用于后面 nSum 的方法

思路：
我们可以把 nums 排序，然后利用双指针来找符合条件的两个数的组合
那么怎么避免得到重复的结果呢，在收缩指针的时候要跳过重复的元素，
这样就能保证每个答案只会被添加一次了

这样一个通用话的 twoSum 的函数就写出来了，可以在后面 nSum 的问题中复用。
复杂度分析：
while 循环的复杂度是 O(N)，排序的复杂度是 O(NlogN)
'''

def twoSum(nums, target):
    res = []
    nums.sort()
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        left_num, right_num = nums[lo], nums[hi]
        summ = left_num + right_num
        if summ == target:
            res.append([left_num, right_num])
            # 移动指针的时候，跳过重复的元素
            while nums[lo] == left_num and lo < hi: lo += 1
            while nums[hi] == right_num and lo < hi:    hi -= 1
        elif summ < target:
            while nums[lo] == left_num and lo < hi: lo += 1
        elif summ > target:
            while nums[hi] == right_num and lo < hi:    hi -= 1
    return res

print(twoSum([1,1,1,2,2,3,3], 4))

        

