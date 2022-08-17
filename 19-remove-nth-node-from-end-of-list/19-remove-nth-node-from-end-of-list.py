# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        c=0
        while temp:
            c+=1
            temp=temp.next
        if c==1 or c==n:
            head=head.next
            return head
        else:
            temp=head
            for i in range(0,c-n-1):
                temp=temp.next
            temp.next=temp.next.next
            return head
        