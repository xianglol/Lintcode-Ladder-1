"""

Merge two sorted (ascending) linked lists and return it as a new sorted list. 
The new sorted list should be made by splicing together the nodes of the two lists and sorted in ascending order.

Example:
Given 1->3->8->11->15->null, 2->null , return 1->2->3->8->11->15->null.

Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param two ListNodes
    @return a ListNode
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        dummy = ListNode(-1)        
        tmp = dummy
        
        while (l1 is not None) and (l2 is not None):
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        if l1 is None:
            tmp.next = l2
        else:
            tmp.next = l1
        return dummy.next