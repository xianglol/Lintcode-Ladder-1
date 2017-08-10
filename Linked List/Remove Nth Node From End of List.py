"""
Given a linked list, remove the nth node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5->null, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5->null.

Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        # define dummy node...            
        dummy = ListNode(-1)
        dummy.next = head
        
        # set two 'pointers', all point to dummy node
        head = dummy
        tmp = dummy

        # move one of the pointers 'head' to place N (the other pointer is still at dummy node)
        for i in range(n):
            head = head.next

        # move two pointers together, until head points to the last node. meanwhile, tmp is pointing to LAST N - 1
        while head.next is not None:
            head = head.next
            tmp = tmp.next

        tmp.next = tmp.next.next

        return dummy.next
