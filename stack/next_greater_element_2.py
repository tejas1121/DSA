class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        st=[]
        n=len(nums)
        ans=[-1]*n
        
        for i in range(2*n):
            c=nums[i%n]
            while st and c>nums[st[-1]]:
                j=st.pop()
                ans[j]=c
                
            if i<n:
                st.append(i)
        return ans        

        