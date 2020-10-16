# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        q = []

        q.append(root)
        depth = 1

        while q:
            sz = len(q)
            for i in range(sz):
                cur = q.pop(0)
                if cur.left == None and cur.right == None:
                    return depth
                if cur.left != None:
                    q.append(cur.left)
                if cur.right != None:
                    q.append(cur.right)
            depth += 1
        return depth