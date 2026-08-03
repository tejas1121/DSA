class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        sorted_freq = sorted(freq.items(), key=lambda x: x[1],reverse=True)
        ans=[]
        for i in range(k):
            ans.append(sorted_freq[i][0])
        return ans    

#By frequency sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        sort_freq=sorted(freq.items(),key=lambda x : x[1],reverse=True)
        ans=[]
        for i in range(k):
            ans.append(sort_freq[i][0])
        return ans    
            

        