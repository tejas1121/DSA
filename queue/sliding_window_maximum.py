from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        dq = deque()
        ans = []

        for i in range(len(nums)):

            # Remove indices outside window


            # Remove smaller elements


            # Add current index


            # Add maximum when window is complete


        return ans