'''
Given a list of words, we may encode it by writing a reference string S and a list of indexes A.

For example, if the list of words is ["time", "me", "bell"], we can write it as S = "time#bell#" and indexes = [0, 2, 5].

Then for each index, we will recover the word by reading from the reference string from that index until we reach a "#" character.

What is the length of the shortest reference string S possible that encodes the given words?

Example:

Input: words = ["time", "me", "bell"]
Output: 10
Explanation: S = "time#bell#" and indexes = [0, 2, 5].
 

Note:

1 <= words.length <= 2000.
1 <= words[i].length <= 7.
Each word has only lowercase letters.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/short-encoding-of-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 用 set 来去掉重复的单词，然后遍历每一个单词，遍历单词的每一个后缀，如果后缀出现在 set 里，
# 就去掉，最后 set 里就没有是其他单词后缀的单词了

# class Solution:
#     def minimumLengthEncoding(self, words) -> int:
#         words_set = set(words)
#         for word in words:
#             for i in range(1, len(word)):
#                 suffix = word[i: ]
#                 words_set.discard(suffix)
#         return len(''.join(words_set)) + len(words_set)

# 字典树，将单词倒序插入到字典树中，那么每个叶子节点就是我们

class Solution:
    def minimumLengthEncoding(self, words) -> int:
        words = list(set(words))
        trie = {}
        nodes = []
        for word in words:
            curr = trie
            for c in reversed(word):
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            nodes.append(curr)
        res = 0
        for word, node in zip(words, nodes):
            if len(node) == 0:
                res += len(word) + 1
        return res



solution = Solution()
print(solution.minimumLengthEncoding(['time', 'me', 'work']))



