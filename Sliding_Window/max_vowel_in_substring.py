class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        w_c=0
        m_c=0
        v=['a','i','e','o','u']
        res=''
        for i in range(k):
              
            if s[i] in v:
                w_c+=1
        m_c=w_c        
        for j in range(k,len(s)):
            if s[j] in v:
                if s[j-k] not in v:
                    w_c+=1
            else:
                if s[j-k] in v:
                    w_c-=1        
            m_c=max(m_c,w_c)
        return m_c            
                


