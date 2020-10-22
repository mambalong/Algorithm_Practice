'''
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# def has_repeat(s):
#     if len(s) > len(set(s)):
#         return True
#     return False

# def lengthOfLongestSubstring(s):
#     n = len(s)
#     res = 0
#     start, end = 0, 0

#     while end < n:
#         tmp = s[start: end+1]
#         while has_repeat(tmp):
#             start += 1
#             tmp = s[start: end+1]
#         end += 1
#         res = max(res, end - start)
#     return res

'''
滑动窗口，我们需要维护一个 window，右指针右移之前要将右指针的元素添加进 window，
左指针右移之前要先把对应的元素移除出 window。
这样就可以计算出每个位置往左看，最长的不重复子串
收缩 window 的判断条件是对应的元素个数大于 1
window 使用的数据结构是 defaultdict
'''
from collections import defaultdict
def lengthOfLongestSubstring(s):
    window = defaultdict(int)
    left, right = 0, 0
    res = 0
    
    while right < len(s):
        c = s[right]
        right += 1
        window[c] += 1
        while window[c] > 1:
            window[s[left]] -= 1
            left += 1
        res = max(res, right - left)
    return res

print(lengthOfLongestSubstring('abcabcbb'))
