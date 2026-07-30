class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        max_area=0
        while i<j:
            width=((j-i)*min(height[i],height[j]))
            max_area=max(width,max_area)
            if height[i]>height[j]:
                j-=1
            else:
                i+=1

        return max_area 
