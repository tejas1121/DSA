class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix=[0]*len(nums)
        prefix[0]=nums[0]
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]+nums[i]
        for i in range(len(nums)):
            if i==0:
                left=0
            else:
                left=prefix[i-1]
            if i==len(nums)-1:
                right=0
            else:
                right=prefix[len(nums)-1]-prefix[i]
            if left==right:
                return i
        return -1                     
