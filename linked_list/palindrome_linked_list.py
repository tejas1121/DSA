class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []

        curr = head

        while curr:
            stack.append(curr.val)
            curr = curr.next

        curr = head

        while curr:
            if curr.val != stack.pop():
                return False
            curr = curr.next

        return True
#two pointer approach
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # Find middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None

        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # Compare
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True    