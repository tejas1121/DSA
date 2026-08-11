Yes. We'll start Pattern 6: Queue today.

Since you've already done Stack, Queue should be straightforward because the main difference is:

Stack → LIFO
Queue → FIFO
Stack

Last In, First Out

push → [1, 2, 3] → pop → 3
Queue

First In, First Out

enqueue → [1, 2, 3] → dequeue → 1
Queue Pattern Roadmap

We'll go from basic → interview level:

232 — Implement Queue using Stacks
225 — Implement Stack using Queues
933 — Number of Recent Calls
622 — Design Circular Queue
649 — Dota2 Senate
239 — Sliding Window Maximum ⭐⭐⭐⭐⭐
→ This introduces the Monotonic Queue, which is the most important advanced queue pattern.

We'll focus on understanding the pattern rather than just memorizing implementations.

First Problem: 232 — Implement Queue using Stacks

The problem asks you to implement:

push(x)
pop()
peek()
empty()

using only stacks.

The important constraint is:

A queue must behave FIFO, but a stack behaves LIFO.

So we need to reverse the order somehow.

Example

Queue:

1 → 2 → 3

Queue pop() should remove:

1

But a stack naturally removes:

3

So we'll use two stacks:

input stack
output stack

The key idea:

Input:
[1,2,3]

Move everything to output:

[3,2,1]

Now pop → 1

That reversal converts LIFO behavior into FIFO behavior.

Your first task

Before we code, tell me:

If we have:

input = [1, 2, 3]

and move all elements from input to output using pop() and append(),

what will output contain?

Think about the order carefully.

first give the theory of queue

Absolutely. Before solving problems, let's build the Queue theory properly.

Pattern 6: Queue

A Queue is a linear data structure that follows:

FIFO — First In, First Out

The element that enters first is the element that leaves first.

Think of a line at a ticket counter:

Person A → Person B → Person C → Person D
   ↑
first to enter

Person A gets served first.

1. Basic Queue Structure

A queue has two important ends:

          Queue
   ┌───────────────────┐
   │  A  B  C  D       │
   └───────────────────┘
   ↑                   ↑
 Front               Rear
Front

The element that will be removed next.

Rear

The position where a new element is inserted.

So:

Insert → Rear
Remove → Front
2. Main Operations

There are four important operations.

Enqueue

Add an element to the rear.

Queue = [1,2,3]

enqueue(4)

Queue = [1,2,3,4]
Dequeue

Remove the element from the front.

Queue = [1,2,3,4]

dequeue()

Queue = [2,3,4]

Returned:

1
Peek / Front

Look at the first element without removing it.

Queue = [2,3,4]

peek() → 2
IsEmpty

Check whether the queue contains anything.

[] → True
3. Queue vs Stack

This is very important for interviews.

	Stack	Queue
Principle	LIFO	FIFO
Insert	Top	Rear
Remove	Top	Front
Example	Stack of plates	People in a line
Python concept	append/pop	append/popleft

Visual:

STACK

   ↓ pop
  [3]
  [2]
  [1]


QUEUE

dequeue ↓

[1] [2] [3]
 ↑       ↑
Front   Rear
4. Queue in Python

The most appropriate built-in structure is:

from collections import deque

Create:

q = deque()

Add:

q.append(10)
q.append(20)
q.append(30)

Queue:

[10,20,30]

Remove from front:

q.popleft()

returns:

10

Queue becomes:

[20,30]

Peek:

q[0]

Check empty:

if not q:
5. Why Not Use a Normal List?

You could write:

q = []

and:

q.append(10)
q.append(20)
q.append(30)

But removing from the front using:

q.pop(0)

is O(n).

Why?

Because all remaining elements have to shift left.

Before:

[10,20,30,40]

pop(0)

[20,30,40]
 ↑
elements shifted

With deque:

q.popleft()

is:

O(1)

So for a proper queue implementation, deque is preferred.

6. Queue Complexity

Using a proper queue/deque:

Operation	Complexity
Enqueue	O(1)
Dequeue	O(1)
Peek	O(1)
Empty	O(1)
7. Types of Queues

There are several queue variants.

Simple Queue

Normal FIFO:

A → B → C → D
Circular Queue

The rear wraps around to the beginning when space becomes available.

       ┌───────────┐
       ↓           │
[A][B][C][ ][ ] ←──┘

We'll encounter this in LeetCode 622.

Priority Queue

Elements are removed according to priority, not simply insertion order.

Example:

Emergency patients

Priority 1 → treated first
Priority 2 → next
Priority 3 → next

This leads into Heap / Priority Queue, which we'll study separately.

Deque

Double-Ended Queue

You can insert/remove from both ends.

← insert/remove    insert/remove →
[ A  B  C  D ]

Python's deque supports this.

q.append(x)       # rear
q.appendleft(x)   # front

q.pop()           # rear
q.popleft()       # front
8. Queue in Algorithms

Queue becomes especially important in BFS (Breadth-First Search).

Imagine a tree:

        1
       / \
      2   3
     / \
    4   5

BFS visits:

1 → 2 → 3 → 4 → 5

We process nodes in the same order they were discovered.

That's exactly FIFO.

So:

Queue
  ↓
BFS
  ↓
Trees
  ↓
Graphs

This is why learning Queue is important before we reach Trees and Graphs.

9. Core Queue Pattern

Most basic queue problems follow:

queue = deque()

# Add
queue.append(x)

# Remove
x = queue.popleft()

# Check front
queue[0]

But interview questions often add another concept on top of the queue:

Queue
  +
Stack
  +
HashMap
  +
Sliding Window
  +
Monotonic structure