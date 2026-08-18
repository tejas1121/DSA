1. What is a Tree?

A Tree is a non-linear data structure used to represent hierarchical relationships.

Unlike an array or linked list, data isn't arranged sequentially.

Examples:

File system
Organization hierarchy
HTML DOM
Database indexes
Decision trees

A tree consists of nodes connected by edges.

Example:

            1
          /   \
         2     3
        / \   / \
       4   5 6   7

Here:

1, 2, 3, ... → Nodes
Lines connecting them → Edges
1 → Root
4, 5, 6, 7 → Leaf nodes
2. Important Terminology
Root

The topmost node.

        1  ← Root
       / \
      2   3

A tree has exactly one root.

Parent

A node directly above another node.

       1
      / \
     2   3

1 is the parent of 2 and 3.

Child

A node directly below another node.

2 and 3 are children of 1.

Siblings

Nodes having the same parent.

       1
      / \
     2   3

2 and 3 are siblings.

Leaf Node

A node with no children.

       1
      / \
     2   3

2 and 3 are leaf nodes.

Internal Node

A node having at least one child.

Here, 1 is an internal node.

3. Edge

An edge is the connection between two nodes.

      1
     /
    2

There is one edge between 1 and 2.

If a tree has N nodes, it always has:

N − 1 edges

For example:

        1
       / \
      2   3
     /
    4

Nodes = 4
Edges = 3

4. Depth

Depth tells us how far a node is from the root.

Usually:

        1          depth = 0
       / \
      2   3        depth = 1
     / \
    4   5          depth = 2

So:

Depth of 1 = 0
Depth of 2 = 1
Depth of 4 = 2
Key idea

Depth = distance from root to node

5. Height

Height tells us how far a node is from its deepest descendant.

For example:

        1
       /
      2
     /
    3

Using edges:

Height of 3 = 0
Height of 2 = 1
Height of 1 = 2

So:

Height of a node = longest path from that node to a leaf

And:

Height of tree = height of root

⚠️ You may see some problems defining height using number of nodes instead of edges. Always check the convention.

6. Subtree

A node and all of its descendants form a subtree.

        1
       / \
      2   3
     / \
    4   5

The subtree rooted at 2 is:

      2
     / \
    4   5

This concept becomes extremely important when we learn recursion.

7. Binary Tree

A Binary Tree is a tree where each node can have at most two children.

Those children are called:

Left child
Right child

Example:

        1
       / \
      2   3
     /
    4

A node can have:

0 children
1 child
2 children

But never more than 2.

8. Binary Tree Node in Python

You'll commonly see:

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

For:

        1
       / \
      2   3

we can represent it as:

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

Think of each node as:

TreeNode
 ├── val
 ├── left
 └── right

This is similar to the way we used next in Linked Lists, except a binary-tree node has two possible references.

9. Types of Binary Trees

These are important for placement tests.

Full Binary Tree

Every node has either:

0 children, or
2 children

Never exactly 1 child.

        1
       / \
      2   3
     / \
    4   5
Complete Binary Tree

Every level is completely filled except possibly the last, and the last level is filled from left to right.

        1
       / \
      2   3
     / \  /
    4  5 6

This concept is particularly important for heaps.

Perfect Binary Tree

Every internal node has exactly two children and all leaves are at the same level.

          1
        /   \
       2     3
      / \   / \
     4   5 6   7

If height is h (using root depth 0):

Number of nodes = 2^(h+1) − 1

Balanced Binary Tree

A tree is balanced when the heights of the left and right subtrees don't differ excessively.

A common interview definition is:

For every node, the height difference between its left and right subtrees is at most 1.

We'll solve Balanced Binary Tree later.

10. Binary Search Tree — BST

This is extremely important.

A Binary Search Tree follows:

              root
             /    \
        smaller   larger

For every node:

Left subtree < Node < Right subtree

Example:

          8
        /   \
       3     10
      / \      \
     1   6      14

For node 8:

left side  < 8
right side > 8

This property makes searching efficient.

Important distinction

Binary Tree:

        8
       / \
      10  3

This is perfectly valid as a binary tree.

But it is not a BST because 10 is on the left of 8.

11. Why Trees Are Important for Placements

Trees combine several concepts you'll need later:

Trees
 ├── Recursion
 ├── DFS
 ├── BFS
 ├── Stack
 ├── Queue
 ├── Binary Search
 ├── Greedy ideas
 └── Graph concepts

In fact, once you understand tree traversal, Graph DFS/BFS becomes much easier.

🧠 The Most Important Mental Model

When you see:

             1
           /   \
          2     3
         / \     \
        4   5     6

Don't think of it as one complicated structure.

Think:

           Node 1
          /      \
      Tree 2     Tree 3

And:

Tree 2
  ├── 2
  ├── 4
  └── 5
Tree 3
  ├── 3
  └── 6

Every node can be treated as the root of its own smaller tree.

That idea is the foundation of recursive tree problems.