class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       l=0
       r=len(numbers)-1
       while l<=r:
         value=numbers[l]+numbers[r]
         if target>value:
            l+=1
         elif target<value:
            r-=1
         else:
            return (l+1,r+1)   
               