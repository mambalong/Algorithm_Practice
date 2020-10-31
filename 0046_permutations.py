'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''


class Solution:
    def permute(self, nums):
      res = []
      def dfs(nums, track):
        if len(track) == len(nums):
          res.append(list(track))
        for num in nums:
          if num in track:
            continue
          track.append(num)
          dfs(nums, track)
          track.pop()
      dfs(nums, [])
      return res
        





