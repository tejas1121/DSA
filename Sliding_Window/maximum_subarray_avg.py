class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        w_sum = 0
        m_sum = 0
        
        for i in range (k):
            w_sum+=nums[i]
        m_sum=w_sum
        l=0    
        for r in range(k,len(nums)):
            w_sum = w_sum - nums[l] + nums[r]
            l+=1
            if w_sum> m_sum :
                m_sum = w_sum
        return m_sum/k
        