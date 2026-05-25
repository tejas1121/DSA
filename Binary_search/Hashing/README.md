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