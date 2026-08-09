class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        mp={}
        for i in nums2:
            while st and i>st[-1]:
                l=st.pop()
                mp[l]=i
              

            st.append(i)
        for j in st:
            mp[j]= -1
        ans=[]
        for k in nums1:
            ans.append(mp[k])
        return ans    

        