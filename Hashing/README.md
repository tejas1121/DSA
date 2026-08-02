🧠 What is Hashing?

Hashing means:

store and retrieve data very fast

Usually:

O(1)

using:

dict
set
Counter
defaultdict

in Python.

| Structure       | Use                           |
| --------------- | ----------------------------- |
| `set()`         | unique elements / fast lookup |
| `dict()`        | key → value mapping           |
| `Counter()`     | frequency counting            |
| `defaultdict()` | auto default values           |





🔥 Hashing Pattern 1 — Frequency Counting

This is one of the most important DSA patterns.

🧠 Core Idea

You store:

element → count
Example
arr = [1,1,2,3,3,3]

Frequency map:

{
  1: 2,
  2: 1,
  3: 3
}
🔥 Why Frequency Counting Matters

Used in:

anagrams
duplicates
majority element
top K frequent
sliding window
prefix sums
🧠 Main Data Structure

Usually:

dict()

or:

Counter()

Method 1 — Manual Frequency Map (IMPORTANT)
Template
freq = {}

for item in arr:
    freq[item] = freq.get(item, 0) + 1
🧠 How .get() Works
freq.get(key, default)

Meaning:

if key exists → return value
else → return default

🔹 Method 2 — Counter (Shortcut)
from collections import Counter

freq = Counter(arr)
Example
Counter([1,1,2,3])

Output:

{1:2, 2:1, 3:1}

FOR SORTING 
sorted_freq = sorted(freq.items(), key=lambda x: x[1],reverse=True) //decending 

The Line
sorted_freq = sorted(
    freq.items(),
    key=lambda x: x[1],
    reverse=True
)

Let's break it down piece by piece.

Step 1: What is freq.items()?

Suppose:

freq = {
    1: 3,
    2: 2,
    3: 1
}

Then:

freq.items()

returns:

dict_items([
    (1, 3),
    (2, 2),
    (3, 1)
])

Think of it as:

[
    (1, 3),
    (2, 2),
    (3, 1)
]

Each tuple is:

(key, value)

or:

(number, frequency)
Step 2: What does sorted() do?

Normally:

sorted(freq.items())

sorts by the first element of each tuple.

Example:

[(3,1), (1,3), (2,2)]

becomes:

[(1,3), (2,2), (3,1)]

because it sorts by the key.

Step 3: What is key=?

key tells Python:

"Before comparing items, use this value."

Example:

sorted(arr, key=...)
Step 4: What is lambda x: x[1]?

A lambda is a small anonymous function.

This:

lambda x: x[1]

means:

def f(x):
    return x[1]
Example

Python processes:

(1,3)

Then:

x = (1,3)
x[1]

returns:

3

For:

(2,2)

returns:

2

For:

(3,1)

returns:

1
So Python Sees

Original:

[(1,3), (2,2), (3,1)]

Sort key values:

3
2
1
Step 5: What does reverse=True do?

Without:

reverse=True

result:

[(3,1), (2,2), (1,3)]

smallest frequency first.

With:

reverse=True

result:

[(1,3), (2,2), (3,1)]

largest frequency first.

Visual Representation
freq = {
    1:3,
    2:2,
    3:1
}

↓

freq.items()

↓

[
    (1,3),
    (2,2),
    (3,1)
]

↓

key=lambda x:x[1]

extracts:

[
    3,
    2,
    1
]

↓

sort by those values

↓

[
    (1,3),
    (2,2),
    (3,1)
]
Other Useful Variations
Sort by key
sorted(freq.items(), key=lambda x: x[0])

Uses:

1
2
3
Sort by frequency
sorted(freq.items(), key=lambda x: x[1])

Uses:

3
2
1


Pattern 1: Frequency Counting
When should this pattern come to your mind?

Whenever the question contains words like:

Count
Frequency
Most frequent
Duplicate count
Majority
Anagram
Occurrences

The Template

This is the template you'll use over and over.

freq = {}

for x in nums:
    freq[x] = freq.get(x, 0) + 1

That's it.

You should be able to write these 4 lines without thinking.
problem solved:
anagram
majority_element
first unique element in string