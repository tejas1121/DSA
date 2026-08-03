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
ransome note
k_most_frequent.py
group anagram




Pattern 2: Lookup / Complement Pattern (Hashing)
Core Idea

In Pattern 1, we asked:

"How many times has this element appeared?"

In Pattern 2, we ask:

"Have I seen this element before?"

or

"Have I already seen the value I need?"

Instead of counting, we're performing fast lookups.

When do we use this pattern?

Whenever the problem contains phrases like:

Does this element exist?
Have we seen this before?
Find a pair.
Find a duplicate.
Check if present.
Return the first repeated element.
Find complement.

Think:

HashSet or HashMap

HashSet vs HashMap
HashSet

Stores only values.

Example:

seen = {2, 5, 8}

Questions it answers quickly:

Is 5 present?
Have I already seen 10?

Operations

5 in seen

Average Time:

O(1)
HashMap (Dictionary)

Stores

Key → Value

Example

student = {
    "Alice": 90,
    "Bob": 85
}

Questions:

Is Alice present?
What is Alice's mark?
Mental Model

Imagine you're checking attendance.

Without hashing

Rahul?
Search all students...

Time

O(n)

With HashSet

Rahul?

Yes

Instant lookup.

General Algorithm
Create empty set/map

Loop through every element

If element already exists

        answer found

Else

        store it

This is the most common pattern.

Example 1

Input

[1,2,3,1]

Initially

seen = {}

Read 1

Not present

Store

seen = {1}

Read 2

Store

seen = {1,2}

Read 3

Store

seen = {1,2,3}

Read 1

Already exists

Duplicate found

Done.

Example 2 (Two Sum)

Suppose

nums = [2,7,11,15]

target = 9

Current number

2

Ask

What number do I need?

9 - 2 = 7

Have we seen 7?

No

Store

2

Next

7

Need

9 - 7 = 2

Have we seen 2?

Yes

Answer found.

Notice:

We never compare every pair.

Why is this fast?

Without hashing

Search every element

O(n)

With hashing

Lookup

O(1)

So many problems improve from

O(n²)

to

O(n)
Common Variations
1. Duplicate Detection
Contains Duplicate

Store values.

2. Complement Search
Two Sum

Store previous values.

3. Previous Occurrence
Contains Duplicate II

Store index.

4. Mapping
Isomorphic Strings

Word Pattern

Store relationships.

5. Presence Checking
Longest Consecutive Sequence

Use a HashSet.

How to recognize Pattern 2 in an interview

If you read a problem and immediately think:

"I need to know whether something already exists."
"I need to find a matching value."
"I need to remember previous elements."
"Searching repeatedly is too slow."

then Pattern 2 (Lookup/Complement using HashSet or HashMap) is likely the right approach.

Pattern 1 vs Pattern 2
Pattern	Main Question	Data Structure	Example Problems
Pattern 1: Frequency Counting	How many times does this appear?	HashMap	Valid Anagram, Top K Frequent Elements, Group Anagrams
Pattern 2: Lookup / Complement	Have I seen this before? Does the required value exist?	HashSet / HashMap	Contains Duplicate, Two Sum, Contains Duplicate I