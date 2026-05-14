class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def first_position():
            low = 0
            high = len(nums) - 1
            ans = -1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] == target:
                    ans = mid
                    high = mid - 1   # search left side

                elif nums[mid] < target:
                    low = mid + 1

                else:
                    high = mid - 1

            return ans

        def last_position():
            low = 0
            high = len(nums) - 1
            ans = -1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] == target:
                    ans = mid
                    low = mid + 1    # search right side

                elif nums[mid] < target:
                    low = mid + 1

                else:
                    high = mid - 1

            return ans

        return [first_position(), last_position()]