class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=''
        for i in s:
            if(i.isalnum()):
                res+=i
        res=res.lower()
        print(res)
        i=0
        j=len(res)-1
        
        while i<=j:
            if (res[i]==res[j]):
                i+=1
                j-=1
                
            else:

                return False        
        return True     