'''
1004. Max Consecutive Ones III
Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s. 

 

Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
Example 2:

Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation: 
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

'''

'''
思路：滑动窗口
窗口内最多有 k 个零，求窗口的最大长度

'''
class Solution:
    def longestOnes(self, A: list[int], K: int) -> int:
        count_0, left, right, res = 0, 0, 0, 0
        while right < len(A):
            if A[right] == 0:
                count_0 += 1
            right += 1
            while count_0 > K:
                if A[left] == 0:
                    count_0 -= 1
                left += 1
            res = max(res, right - left)
        return res

