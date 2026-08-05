class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        prefix=0
        
        mp={0:1}
        count=0
        for i in range(n):
            prefix+=nums[i]
            c=prefix%k
            if c in mp:
                count+=mp[c]
            
            mp[c]=mp.get(c,0)+1
        return count      
        