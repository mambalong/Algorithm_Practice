'''
116. Populating Next Right Pointers in Each Node
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:

    def connectTwoNodes(self, node1, node2):
        if node1 == None and node2 == None:
            return
        # 先把两个 node 连起来
        node1.next = node2
        # 把两个 node 的左右字节点连起来
        self.connectTwoNodes(node1.left, node1.right)
        self.connectTwoNodes(node2.left, node2.right)
        # 把node1的右字节点和node2的做子节点连起来
        self.connectTwoNodes(node1.right, node2.left)

    def connect(self, root):
        if root == None:
            return
        self.connectTwoNodes(root.left, root.right)
    