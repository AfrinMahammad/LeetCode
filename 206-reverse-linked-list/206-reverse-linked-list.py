# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        pres=head
        while pres:
            temp=pres.next
            pres.next=prev
            prev=pres
            pres=temp
        return prev