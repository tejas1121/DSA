🧠 What Binary Search REALLY Is

Most beginners think:

“binary search = find element in sorted array”

That’s only the beginning.

Real binary search is:

searching an answer space efficiently

Type 1: Exact Search
🧩 Goal

Find exact element

Example
Binary Search (#704)
Pattern
if nums[mid] == target:
🔹 Type 2: First / Last Occurrence
🧩 Goal

Find boundaries

Example
Find First and Last Position of Element in Sorted Array (#34)
Key Insight
When target found:
👉 DON’T stop

First Occurrence
ans = mid
high = mid - 1
Last Occurrence
ans = mid
low = mid + 1
🔹 Type 3: Lower Bound / Upper Bound

VERY IMPORTANT for interviews.

🧠 Lower Bound

Find:

first element >= target
🧠 Upper Bound

Find:

first element > target
Example
Search Insert Position
Floor/Ceil problems
🔹 Type 4: Binary Search on Answer ⭐ MOST IMPORTANT

This is advanced and VERY common.

🧠 Idea

You are NOT searching array.

You are searching:

possible answer range
Example Problems
Problem	Search Space
Koko Eating Bananas	eating speed
Capacity to Ship Packages	ship capacity
Minimum Days to Make Bouquets	number of days
🔥 Example: Koko Eating Bananas

👉 Can Koko finish at speed = 5?

If YES:

maybe smaller speed also works

If NO:

need bigger speed
🧠 This creates monotonic behavior
FFFFFTTTTT

👉 Perfect for binary search

🔹 Type 5: Rotated Sorted Array
Example
Search in Rotated Sorted Array
🧠 Key Insight

At least ONE half is always sorted

🔹 Type 6: Peak / Mountain Problems
Example
Find Peak Element
Peak Index in Mountain Array
🧠 Key Insight

Use neighboring comparisons:

nums[mid] < nums[mid+1]
🔥 Most Important Binary Search Skill

Not coding.

👉 Identifying:

Can search space be divided?
🧠 Recognition Signals

Use binary search when:

Signal	Meaning
sorted array	classic BS
minimum possible / maximum possible	answer search
monotonic behavior	YES/NO transition
search efficiently	likely BS
⚠️ Common Mistakes
❌ Infinite Loop

Wrong:

high = mid

Correct:

high = mid - 1

❌ Wrong Loop Condition

Usually:

while low <= high
❌ Forgetting answer storage

For boundary problems:

ans = mid
🧠 Golden Mental Model

Binary Search =

Shrink search space intelligently
🚀 Recommended Learning Order
Phase 1 — Basics
#704 Binary Search
#35 Search Insert Position
#34 First and Last Position
Phase 2 — Variations
Rotated Sorted Array
Find Minimum in Rotated Array
Peak Element
Phase 3 — Binary Search on Answer
Koko Eating Bananas
Capacity to Ship Packages
Split Array Largest Sum
