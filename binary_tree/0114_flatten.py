'''
114. 二叉树展开为链表
给定一个二叉树，原地将它展开为一个单链表。

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return
        # 将左右子树分别拉直
        self.flatten(root.left)
        self.flatten(root.right)

        # 将左子树变成右子树
        right = root.right
        root.right = root.left
        root.left = None

        # 将右子树接在左子树的下面
        tmp = root
        while tmp.right != None:
            tmp = tmp.right
        tmp.right = right




