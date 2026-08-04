class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
    
        c_w={}
        w_c={}
        word=s.split()
        if len(pattern)!=len(word):
            return False
        for i in range(len(pattern)):
            if pattern[i] in c_w:
                if c_w[pattern[i]]!=word[i]:
                    return False
            else:
                c_w[pattern[i]]=word[i]
            if  word[i] in w_c:
                if w_c[word[i]]!=pattern[i]:
                    return False
            else:
                w_c[word[i]]=pattern[i]        

           
        return True            
        