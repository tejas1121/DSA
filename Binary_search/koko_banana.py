import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canEat(speed):
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / speed)

            return hours <= h

        low = 1
        high = max(piles)

        while low < high:
            mid = (low + high) // 2

            if canEat(mid):
                high = mid
            else:
                low = mid + 1

        return low