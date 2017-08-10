"""
Remove Linked List Elements
Example
Given 1->2->3->3->4->5->3, val = 3, you should return the list as 1->2->4->5

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return a ListNode
    def removeElements(self, head, val):
        # Write your code here
        
        # Define dummy node, val -1(could be any), next node point to head
        dummy = ListNode(-1)
        dummy.next = head

        # Head points to dummy node
        head = dummy

        # Traverse the linked list
        while head.next is not None:
            if head.next.val == val:
                head.next = head.next.next
            else:
                # Move to next node
                head = head.next
        return dummy.next