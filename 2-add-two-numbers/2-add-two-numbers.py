# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x,y=[],[]
        while l1 is not None:
            x.append(str(l1.val))
            l1=l1.next
        while l2 is not None:
            y.append(str(l2.val))
            l2=l2.next
        s1=int(''.join(x[::-1]))
        s2=int(''.join(y[::-1]))
        l=[]
        for i in str(s1+s2):
            l.append(i)
        l.reverse() 
        res=ListNode()
        temp=res
        for i in range(0,len(l)):
            temp.next=ListNode(int(l[i]),None)
            temp=temp.next
        res=res.next    
        return res