"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: The head of linked list.
    @param: val: An integer.
    @return: The head of new linked list.
    """

    def insertNode(self, head, val):
        # write your code here
        dummy = ListNode(0)
        node = ListNode(val)
        
        dummy.next = head
        head = dummy
        
        while head.next != None and head.next.val <= val:
            head = head.next
        
        node.next = head.next
        head.next = node
        
        return dummy.next