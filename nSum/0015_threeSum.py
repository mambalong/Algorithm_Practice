'''
15. 3Sum
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''

class Solution:

    def twoSum(self, nums, target):
        res = []
        nums.sort()
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            left_num, right_num = nums[lo], nums[hi]
            summ = left_num + right_num
            if summ == target:
                res.append([left_num, right_num])
                while left_num == nums[lo] and lo < hi: lo += 1
                while right_num == nums[hi] and lo < hi: hi -= 1
            elif summ < target:
                while left_num == nums[lo] and lo < hi: lo += 1
            elif summ > target:
                while right_num == nums[hi] and lo < hi: hi -= 1
        return res

    def threeSumTarget(self, nums, target):
        res = []
        nums.sort()
        for index, num in enumerate(nums):
            if index != 0 and num == nums[index-1]:
                continue
            new_target = target - num
            for i in self.twoSum(nums[index+1: ], new_target):
                res.append([num] + i)
        return res
    
    def threeSum(self, nums):
        return self.threeSumTarget(nums, 0)

solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))

            