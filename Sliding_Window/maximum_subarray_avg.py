class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        w_sum = 0

        for i in range(k):
            w_sum += nums[i]

        m_sum = w_sum

        for j in range(k, len(nums)):
            w_sum += nums[j] - nums[j-k]
            m_sum = max(m_sum, w_sum)

        return m_sum / k