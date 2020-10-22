'''
567. Permutation in String

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Constraints:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-in-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
思路：

这是一个滑动窗口问题，还是可以通过维护一个 need 字典来做，need[c] 的值就代表当前窗口还需要多少个 c，
负值就代表多余，老样子，判断窗口需要收缩的条件是，need_cnt = 0，它代表了还需要的元素的个数，我们维护
need 的同时也要维护 need_cnt。

注意判断结果的位置，应当是开始收缩窗口的 while 循环里面的第一步。

'''

from collections import defaultdict
def checkInclusion(s1, s2):
    need_cnt = len(s1)
    need = defaultdict(int)
    for c in s1:
        need[c] += 1

    left, right = 0, 0

    while right < len(s2):
        c = s2[right]
        right += 1
        if need[c] > 0:
            need_cnt -= 1
        need[c] -= 1

        while need_cnt == 0:
            if right - left == len(s1):
                return True
            c = s2[left]
            left += 1
            need[c] += 1
            if need[c] > 0:
                need_cnt += 1
    return False
print(checkInclusion("ab", "eidboaoo"))
