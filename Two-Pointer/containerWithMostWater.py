class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        maxi=0
        
        while i<j:
            
            area = ((j-i)*min(height[i],height[j]))
            maxi=max(maxi,area)

            if (height[i]>height[j]):
                j= j-1
            else:
                i=i+1
        return maxi            
