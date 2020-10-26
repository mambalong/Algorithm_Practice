'''
206. Reverse Linked List
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 迭代法
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        nex = None

        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre

# 递归法
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p