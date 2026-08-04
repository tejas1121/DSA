Pattern 3: Prefix Sum

This is one of the most important DSA patterns.

Core Idea

Instead of asking:

"Have I seen this value before?" (Pattern 2)

we ask:

"What is the sum of all elements up to this point?"

That running total is called the prefix sum.

What is a Prefix Sum?

Given

nums = [2, 4, 1, 6, 3]

The prefix sum array is

Index	Number	Prefix Sum
0	2	2
1	4	6
2	1	7
3	6	13
4	3	16

Meaning:

prefix[0] = 2
prefix[1] = 2+4 = 6
prefix[2] = 2+4+1 = 7
prefix[3] = 2+4+1+6 = 13
prefix[4] = 2+4+1+6+3 = 16
Why do we need it?

Suppose I ask:

What is the sum from index 1 to 3?

Without a prefix sum:

4 + 1 + 6

You compute it every time.

Time:

O(n)

With a prefix sum:

Sum(1...3)
=
prefix[3] - prefix[0]
13 - 2 = 11

Done.

Time:

O(1)
Formula

If

prefix[i]

means

sum from index 0 to i

Then

Sum(L...R)

=

prefix[R] - prefix[L-1]

Example

nums

2 4 1 6 3

Need

1...4
4+1+6+3

Using prefix

16 - 2 = 14

Correct.

Visual Understanding
Array

2   4   1   6   3
0   1   2   3   4

Prefix

2   6   7   13  16

Need

index 2 to 4

1 + 6 + 3

Take

16

Remove

2+4 = 6

Answer

16 - 6 = 10
Why is it called "Prefix"?

Because every value stores the sum of the prefix (beginning) of the array.

Prefix till index 0

2
Prefix till index 2

2+4+1
Prefix till index 4

2+4+1+6+3
Building Prefix Sum

Suppose

nums = [5,2,7,4]

Start

prefix = [0]*4
prefix[0]=5

Now

prefix[1]=5+2=7
prefix[2]=7+7=14
prefix[3]=14+4=18

Result

[5,7,14,18]
General Algorithm
prefix[0] = nums[0]

for i in range(1, n):
    prefix[i] = prefix[i-1] + nums[i]
Where Prefix Sum is Used

Whenever you see questions like:

Sum of a subarray
Range sum queries
Continuous subarray
Subarray sum equals K
Equal prefix/suffix
Pivot index

Think:

Prefix Sum