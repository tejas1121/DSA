class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
         freq={}
         for i in magazine:
            freq[i]=freq.get(i,0)+1
         for ch in ransomNote:
            if ch not in freq:
                return False
            freq[ch]-=1
            if freq[ch]<0:
                return False
         return True       
