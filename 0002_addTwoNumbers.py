
'''
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

'''

'''
思路，就是按照加法一位一位来做，可以不用补零，只需要把加两个数分开来算就好了，如果不够长了，
就是说需要补零的位置，对应的 node 就是 None 了，只需要判断 Node 是不是 None，不是就加上 val，
否则不加。
注意最后要判断 carry 是不是零，最后还有进位的话要加上。
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res_head = ListNode()
        head = res_head
        carry = 0
        while l1 or l2:
            summ = carry
            if l1 != None:
                summ += l1.val
                l1 = l1.next
            if l2 != None:
                summ += l2.val
                l2 = l2.next
            carry = summ // 10
            summ = summ % 10
            head.next = ListNode(val=summ)
            head = head.next
        if carry:
            head.next = ListNode(val=carry)
        return res_head.next
