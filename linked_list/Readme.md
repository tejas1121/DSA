Pattern 7: Linked List

Before solving LeetCode problems, you need to understand what a linked list actually is, why it exists, and how it differs from an array.

1. What is a Linked List?

A Linked List is a linear data structure where elements are stored inside separate objects called nodes.

Each node contains two things:

┌───────────────┐
│     Node      │
├─────────┬─────┤
│  value  │ next│
└─────────┴─────┘
value

Stores the actual data.

next

Stores a reference/address to the next node.

So unlike an array, the elements don't have to be stored next to each other in memory.

2. Simple Example

Suppose we want to store:

10, 20, 30

A linked list looks like:

10       20       30
┌─────┐  ┌─────┐  ┌─────┐
│ 10  │  │ 20  │  │ 30  │
│  •──┼─→│  •──┼─→│  •──┼─→ None
└─────┘  └─────┘  └─────┘

The arrows represent the next reference.

So:

10.next → Node containing 20

20.next → Node containing 30

30.next → None
3. What is a Node?

In Python, we generally define a node like this:

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

Now:

node1 = ListNode(10)
node2 = ListNode(20)
node3 = ListNode(30)

Currently they are separate:

node1       node2       node3

10          20          30

We connect them:

node1.next = node2
node2.next = node3

Now:

10 → 20 → 30 → None
4. What is head?

This is extremely important.

The linked list needs a way to know where it starts.

That starting node is called:

Head

Example:

head
 ↓
10 → 20 → 30 → None

In Python:

head = node1

So:

head.val

gives:

10

and:

head.next

gives the node containing:

20
5. How Do We Traverse a Linked List?

Unlike an array, we can't simply do:

list[5]

Instead, we follow the next references.

Start at:

head
 ↓
10 → 20 → 30 → None

Use:

current = head

Then:

while current:
    print(current.val)
    current = current.next

Output:

10
20
30

The key line is:

current = current.next

This moves us to the next node.

6. Visualizing Traversal

Initially:

head
 ↓
10 → 20 → 30 → None

current = head

current
   ↓
10 → 20 → 30 → None

Then:

current = current.next

Now:

head
 ↓
10 → 20 → 30 → None
      ↑
    current

Again:

current = current.next

Now:

head
 ↓
10 → 20 → 30 → None
           ↑
         current

Again:

current = current.next

Now:

head
 ↓
10 → 20 → 30 → None
                 ↑
               current

None means we've reached the end.

7. Linked List vs Array

This is one of the most important differences.

Array
[10][20][30][40][50]

Elements are stored in contiguous memory.

You can directly access:

arr[3]

in:

O(1)
Linked List
10 → 20 → 30 → 40 → 50

The nodes can be located anywhere in memory.

To reach 40, we must follow:

head
 ↓
10
 ↓
20
 ↓
30
 ↓
40

Therefore accessing the kth node takes:

O(n)
8. Why Use a Linked List?

The major advantage is insertion and deletion.

Suppose:

10 → 20 → 30

We want to insert 15 between 10 and 20.

With a linked list:

10 → 15 → 20 → 30

We change references.

Conceptually:

10.next = 15
15.next = 20

We don't need to shift every element.

9. Insertion

Suppose:

10 → 20 → 30

We have a node:

15

We want:

10 → 15 → 20 → 30

First:

new.next = current.next

So:

15 → 20

Then:

current.next = new

Now:

10 → 15 → 20 → 30

The order of these two operations matters.

10. Deletion

Suppose:

10 → 20 → 30

We want to delete 20.

We need:

10 → 30

So instead of making 10 point to 20:

10 → 20

we make:

10 → 30

Conceptually:

current.next = current.next.next

That's a very important linked-list operation.

11. Time Complexity

For a singly linked list:

Operation	Complexity
Access by index	O(n)
Search	O(n)
Insert at head	O(1)
Delete at head	O(1)
Insert after known node	O(1)
Delete after known node	O(1)
Insert at end	O(n)*

*Without a tail pointer. With a maintained tail pointer, insertion at the end can be O(1).

The important distinction is:

Linked lists are good at pointer/reference manipulation, but bad at random access.

12. Types of Linked Lists

There are three major types we'll encounter.

Singly Linked List

Each node points only forward:

10 → 20 → 30 → None

Each node has:

value
next

This is what we'll start with.

Doubly Linked List

Each node has two references:

None ← 10 ⇄ 20 ⇄ 30 → None

Each node has:

value
next
prev

This allows us to move:

forward →

and:

← backward

This becomes important for problems like LRU Cache.

Circular Linked List

The last node points back to the first:

10 → 20 → 30
↑         ↓
└─────────┘

There is no None at the end.

We'll encounter circular structures later.

13. The Most Important Linked List Variables

When solving problems, you'll constantly see:

head

The beginning of the list.

head
 ↓
1 → 2 → 3
current

Used to traverse.

current = head
prev

Keeps track of the previous node.

prev    current
 ↓         ↓
1    →    2    →    3

This becomes extremely important when reversing a linked list.

next

The next node.

current.next
14. The Most Important Mental Model

When working with a linked list, don't think about indexes first.

Think about:

NODE → NODE → NODE → NODE

and ask:

Which node is pointing to which node?

For example:

1 → 2 → 3 → 4

If you want to reverse it:

4 → 3 → 2 → 1

you aren't moving array elements.

You're changing the direction of the arrows.

That's the central idea behind many linked-list problems.

15. The Classic ListNode

You'll see this constantly on LeetCode:

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

When LeetCode gives you:

head

you should understand:

head
 ↓
[Node] → [Node] → [Node] → None

Not:

head = 5

head is a reference to a node.

16. Important Python Concept

Suppose:

current = head

Then:

current = current.next

does not change head.

It only moves current.

Example:

head
 ↓
10 → 20 → 30
 ↑
current

After:

current = current.next

we get:

head
 ↓
10 → 20 → 30
      ↑
    current

head still points to 10.

This distinction is crucial when traversing linked lists.