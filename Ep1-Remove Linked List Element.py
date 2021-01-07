#Problem Statement
'''
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5


'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        #What if head has to be deleted?
        while head!=None and head.val == val:
            head = head.next
        #For a middle element that has to be deleted
        temp = head
        while temp!=None and temp.next!=None:
            while temp.next!=None and temp.next.val==val:
                temp.next = temp.next.next
            temp = temp.next
        return head