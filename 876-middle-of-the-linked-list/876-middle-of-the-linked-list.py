# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        temp=ListNode()
        temp=head
        while temp.next is not None:
            c+=1
            temp=temp.next
        if c%2==0:
            c=c//2
        else:
            c=(c//2)+1
        i=0
        while i<c:
            head=head.next
            i+=1
        return head