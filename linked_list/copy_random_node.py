class Solution:
    def copyRandomList(self, head):

        mp = {None: None}

        # Pass 1: create copies
        curr = head

        while curr:
            mp[curr] = Node(curr.val)
            curr = curr.next

        # Pass 2: connect next and random
        curr = head

        while curr:
            copy = mp[curr]

            copy.next = mp[curr.next]
            copy.random = mp[curr.random]

            curr = curr.next

        return mp[head]