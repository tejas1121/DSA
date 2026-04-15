'''
Remove all occurrences of a value in-place
'''

nums = [3, 2, 5, 3,5,4,6,5,4]
val = 5
def removeElement(nums, val):
    i=0
    for j in range (len(nums)):
        if (nums[j]!=val):
            nums[i]=nums[j]
            i+=1
    print(nums)        
    return i
    
print(removeElement(nums, val)) 