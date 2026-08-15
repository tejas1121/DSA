# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head

        count=0
        while curr:
            curr=curr.next
            count+=1
        mid=count//2
        mid_node=head
        for i in range(mid):
            mid_node=mid_node.next
        return mid_node    
#slow and fast pointer approach
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
        