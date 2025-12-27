# Data Structures

## Arrays

### Unsorted Array

### Sorted Array

### Sparse Table

### Stack

### Single Sided Queue

### Double Sided Queue

## Lists

### Singly Sided Linked List
Each node stores values as well as the pointer to the next node.

Operations:

Reverse: O(n)

Space:

O(n) number of nodes in the linked list

Problems:

https://leetcode.com/problems/remove-linked-list-elements/

https://leetcode.com/problems/reverse-linked-list/

### Doubly Sided Linked List

Problems:

https://leetcode.com/problems/lru-cache

https://leetcode.com/problems/lfu-cache


### Ordered Dictionary

Problems:

https://leetcode.com/problems/lru-cache

https://leetcode.com/problems/lfu-cache

## Heaps

### Binary Heap
Complete binary tree stored in an array

Time Complexity: 

Operations:

Insert: O(log(n))

Find Min/Max: O(1)

Extract Min/Max: O(log(n))

Decrease Key: O(log(n))

Merge/Union: O(n)

Delete: O(log(n))

Problems:

https://leetcode.com/problems/meeting-rooms-iii

### Fibonacci Heap
Collection of heap ordered trees with lazy merging.

Time Complexity: 

Operations:

Insert: O(1) amortised

Find Min/Max: O(1)

Extract Min/Max: O(log(n)) amortised

Decrease Key: O(1) amortised

Merge/Union: O(1) amortised

Delete: O(log(n)) amortised

## Trees

### Binary Tree

### Order Statistics Tree

### Fenwick Tree

### B Tree

### Splay Tree

### Red Black Tree

### AVL Tree

### Interval Tree

### Segment Tree

### KD Tree

### Trie

### Treap

### Suffix Tree

### Quick Find
Find checks the parent of the node. Union sets all nodes in one group to belong to the other group.

Time Complexity: 

Operations:

Find: O(1)

Union: O(n)


### Quick Union
Attach one tree under another tree when unioning. To check if two nodes are in the same tree, check if they have the same parent.

Time Complexity: 

Operations:

Find: O(n) 

Bad inputs, worse case degenerates into a chain.

Union: O(n)

Bad inputs, worse case degenerates into a chain.


### Union Find
Same as Quick Union with a small difference.
Maintain the sizes of the nodes, attach the smaller tree under the root of the bigger tree.

Time Complexity: 

Operations:

Find: O(log(n))

Union: O(log(n))

Initialisation: O(n)

Setting parent of each element to itself

### Union Find With Path Compression
Same as Union Find with a small difference.
During the find operation, make every node on the path point to the root.

Time Complexity: 

Operations:

Find: O(α(n)) where α(n) is the ackermann function(effectively constant)

Union: O(α(n)) where α(n) is the ackermann function(effectively constant)

Initialisation: O(n)

Setting parent of each element to itself

Problems:

https://leetcode.com/problems/redundant-connection/

https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph

https://leetcode.com/problems/satisfiability-of-equality-equations

https://adventofcode.com/2025/day/8

## Graphs

### Adj List
For each vertex v, adj_list[v] stores references to vertices that v is connected to.

For an undirected graph for arbitrary unique vertices v1, v2, iff v2 in adj_list[v1] then v1 in adj_list[v2].

### Adj Matrix

