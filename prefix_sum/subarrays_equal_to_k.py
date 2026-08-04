class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        prefix=0
        
        mp={0:1}
        count=0
        for i in range(n):
            prefix+=nums[i]
            c=prefix-k
            if c in mp:
                count+=mp[c]
            
            mp[prefix]=mp.get(prefix,0)+1
        return count                



        