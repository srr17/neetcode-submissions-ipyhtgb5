# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        curr=dummy
        c=0
        while l1 and l2:
            x=l1.val+l2.val+c
            c=int(x/10)
            value=x%10
            node=ListNode(val=value,next=None)
            curr.next=node
            curr=curr.next
            l1=l1.next
            l2=l2.next
        while l1:
            x=l1.val+c
            c=int(x/10)
            value=x%10
            node=ListNode(val=value,next=None)
            curr.next=node
            curr=curr.next
            l1=l1.next
        while l2:
            x=l2.val+c
            c=int(x/10)
            value=x%10
            node=ListNode(val=value,next=None)
            curr.next=node
            curr=curr.next
            l2=l2.next
        if c:
            node=ListNode(val=c,next=None)
            curr.next=node
            
        return dummy.next
        