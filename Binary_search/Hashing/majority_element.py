class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        for n in nums:
            freq[n]=freq.get(n,0)+1
        l=len(nums)
        for n in freq:
            if (freq[n]>l//2):
                return n
            