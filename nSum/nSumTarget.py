'''
这里写一个 nSum 通用的模版
所有的 nums 都要先排序
'''

class Solution:
    def twoSumTarget(self, nums, target):
        res = []
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

    def nSumTarget(self, n, nums, target):
        if n == 2:
            return self.twoSumTarget(nums, target)
        while n > 2:
            res = []
            for index, num in enumerate(nums):
                if index != 0 and num == nums[index-1]:
                    continue
                sub = self.nSumTarget(n-1, nums[index + 1:], target - num)
                for i in sub:
                    res.append([num] + i)
            return res

solution = Solution()
nums = sorted([1,0,-1,0,-2,2])
print(solution.nSumTarget(4, nums, 0))
                
            