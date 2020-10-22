'''
438. Find All Anagrams in a String

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not 
be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''

from collections import defaultdict
def findAnagrams(s, p):
    need_cnt = len(p)
    need = defaultdict(int)
    for c in p:
        need[c] += 1

    res = []
    left, right = 0, 0

    while right < len(s):
        c = s[right]
        right += 1
        if need[c] > 0:
            need_cnt -= 1
        need[c] -= 1
        
        while need_cnt == 0:
            if right - left == len(p):
                res.append(left)
            c = s[left]
            left += 1
            need[c] += 1
            if need[c] > 0:
                need_cnt += 1
    return res

print(findAnagrams("cbaebabacd", "abc"))