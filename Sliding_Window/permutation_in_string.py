class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        mp={}
        need={}
        for i in range(len(s1)):
            mp[s1[i]]=mp.get(s1[i],0)+1
        for j in range(len(s1)):
            need[s2[j]]=need.get(s2[j],0)+1
        if need==mp:
            return True
        for r in range (len(s1),len(s2)):
            need[s2[r]]=need.get(s2[r],0)+1
            left = s2[r - len(s1)]

            need[left] -= 1

            if need[left] == 0:
                del need[left]
            if need==mp:
                return True
        return False        


            
           
        
        