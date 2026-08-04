class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        prefix=[0]*n
        prefix[0]=nums[0]
        for i in range(1,n):
            prefix[i]=prefix[i-1]+nums[i]
        mp={0:1}
        count=0
        for i in range(n):
            c=prefix[i]-k
            if c in mp:
                count+=mp[c]
            
            mp[prefix[i]]=mp.get(prefix[i],0)+1
        return count                



        