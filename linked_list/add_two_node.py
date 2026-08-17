# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=l1
        curr2=l2
        dummy=ListNode(0)
        tail=dummy
        carry=0

        while curr1 or curr2 or carry:
            if curr1:
                v1=curr1.val
            else:
                v1=0
            if curr2:
                v2=curr2.val
            else:
                v2=0
            total=v1+v2+carry
            digit=total%10
            carry=total//10
            tail.next=ListNode(digit)
            tail=tail.next
            if curr1:
                curr1=curr1.next
            if curr2:
                curr2=curr2.next
        return dummy.next            


