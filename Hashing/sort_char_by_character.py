class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        for i in s:
            freq[i]=freq.get(i,0)+1
        sort_freq=sorted(freq.items(),key=lambda x:x[1],reverse=True)
     
        ans=''
        char=''
        for ch,count in sort_freq:
            
            ans+=ch*count
        return ans        
        