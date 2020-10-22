'''
76. Minimum Window Substring

Given a string S and a string T, find the minimum window in S which will contain all the 
characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-window-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
滑动过程中维护一个 need 的字典，need[c] 的值就代表当前窗口还要多少个 c，为负则是多余，为零则是不需要。
收缩窗口需要判断的是 need 中所有的元素都小于等于零，就是不需要任何元素了，但是不能直接这样判断，会增加复杂度。
我们可以用一个变量 need_cnt 来储存还需要元素的数量，当 c 是需要的元素时，need_cnt - 1，need[c] -= 1，
注意，要先 need_cnt - 1，因为判断 c 是否需要要看 need[c] 的值。
'''

from collections import defaultdict
def minWindow(s, t):
    need_cnt = len(t)
    need = defaultdict(int)
    for i in t:
        need[i] += 1
    
    res = float("inf")
    left, right = 0, 0
    start, end = 0, 0
    
    while right < len(s):
        # c 是加入 window 的字符
        c = s[right]
        right += 1
        # 维护 need 和 need_cnt
        if need[c] > 0:
            need_cnt -= 1
        need[c] -= 1
        while need_cnt == 0:
            if res > right - left:
                res = right - left
                start, end = left, right
            c = s[left]
            left += 1
            need[c] += 1
            if need[c] > 0:
                need_cnt += 1

    return s[start: end]

print(minWindow("ADOBECODEBANC", "ABC"))
        
        