class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True            
        i=0
        j=len(s)-1
        count = 0
        while i<=j:

            
                if s[i]==s[j]:
                    i+=1
                    j-=1
                else:
                    return(
                        helper(i,j-1) or
                        helper(i+1,j)
                    )
                    
        return True                
