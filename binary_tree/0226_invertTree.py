'''
226. Invert Binary Tree
Invert a binary tree.
'''

'''
很简单，要反转一个二叉树，我们只需要把每个节点的左右子数交换就好了
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root