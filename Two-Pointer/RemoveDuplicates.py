from rpds import List

def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        for j in range(1, len(nums)):
            if nums[j] != nums[i - 1]:
                nums[i] = nums[j]
                i += 1
        
        return i

'''
Dry Run Example
Input:
nums = [1, 1, 2, 2, 3]
Initial State
Index	0	1	2	3	4
nums	1	1	2	2	3
i = 1
j = 1 → start
🔁 Iteration 1 (j = 1)
nums[j] = 1
nums[i-1] = nums[0] = 1

👉 Duplicate → skip

i = 1 (no change)
🔁 Iteration 2 (j = 2)
nums[j] = 2
nums[i-1] = nums[0] = 1

👉 New element ✅

nums[i] = nums[j]
nums[1] = 2
i = 2
Array now:
[1, 2, 2, 2, 3]
🔁 Iteration 3 (j = 3)
nums[j] = 2
nums[i-1] = nums[1] = 2

👉 Duplicate → skip

i = 2
🔁 Iteration 4 (j = 4)
nums[j] = 3
nums[i-1] = nums[1] = 2

👉 New element ✅

nums[2] = 3
i = 3
Array now:
[1, 2, 3, 2, 3]
'''