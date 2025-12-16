# Algorithms

## Number Theory

### Greatest Common Divisor (Euclidean Algorithm)
Subtract smaller number from larger number, GCD of both numbers remain the same.
Hence, recursively subtract smaller from larger number. This can be done via the modulus operation.

Time Complexity: O(log(min(n, m)))

Space Complexity: O(1)

Problems:

https://leetcode.com/problems/find-greatest-common-divisor-of-array/

### Lowest Common Multiple

### Sqrt Decomposition

### Sieve of Eratosthenes

## Strings

### Rabin-Karp (String Matching)

### Knuth Morris Pratt (String Matching)

## Shuffling

### Reservoir Shuffling

### Fisher-Yates/Knuth Shuffling

## Combinatorics 

### Combinations

Time Complexity: 

Θ(C(n, k)*k) From outputting all combinations with a maximum of k elements(copying) each

Space Complexity:

O(k) from function call stack size equal to max recursive depth which is the number of elements to choose from

Problems:

https://leetcode.com/problems/combinations/

### Permutations
Time Complexity: 

O(n * n!) (approximation)

O((n^2) * (e * Γ(n + 1, 1) -n!)) (better approximation by counting number of nodes in dfs tree)

Space Complexity: 

O(n) from function call stack size equal to max recursive depth which is the number of elements to permute over

Problems:

https://leetcode.com/problems/permutations/


### Subsets

## Searching

### Linear Search 

### Binary Search

### Ternary Search

### Quick Select

### Newton's Method

## Sorting

### Bubble Sort

### Selection Sort

### Insertion Sort

### Merge Sort

### Quick Sort

## Trees

### Build Binary Tree From Array

### Pre Order Traversal (Binary Tree)

### In Order Traversal (Binary Tree)

### Post Order Traversal (Binary Tree)

### Vertex Cover

### Lowest Common Ancestor

## Dynamic Programming

### 0/1 Knapsack

### Unbounded Knapsack

### Bounded Knapsack

## Graphs

### Find Number of Connected Components

### BFS

### DFS

### A-Star

### Kahn's Algorithm (Topological Sort)

### Topological Sort DFS

### Prim's Algorithm

### Kruskal's Algorithm 

### Dijkstra's Algorithm

### Bellman Ford

### Floyd Warshall

### K-Nearest Neighbours

### Bron-Kerbosch (Maximal clique)

### Find Bridges

### Eulerian Path

### Hamiltonian Cycle

### Edmonds Karp (Maximum Flow)

### Kuhn's Algorithm (Max Bipartite Matching)

### 2-SAT

## Randomness

### Linear Congruential Generator (LCG)

## Cycle Detection

### Tortoise and Hare Algorithm
Used to detect cycles in a linked list. Have two pointers traversing the linked list, one faster and one slower.
If there is a cycle, the faster pointer will point to an earlier node and eventually meet the slower pointer.
If there is no cycle, the faster pointer will find the ending node and return that there is no cycle.


Time Complexity: 

O(n)

Slower pointer enters the cycle after x steps. Faster pointer enters at <= x steps, since it moves faster.
in a cycle of y length, the distance between the two pointers decreases by 1 each iteration.
So the max number of iterations for both pointers to meet in the cycle is y.
Hence, number of iterations <= y + x <= n. Since each iteration is O(1), for n iterations, time complexity is O(n)

Space Complexity:

O(1)

Problems:

https://leetcode.com/problems/linked-list-cycle/

## Linear Equations

### Gaussian-Jordan Method 

### Linear Programming

### Integer Linear Programming

## Optimisation

### Minimax

### Negamax

### Simulated Annealing

## Geometry 

### Convex Hull

## Matrices

### Rotate Matrix Clockwise by 90 degrees

### Transpose Matrix

## ETC

### Line Sweep

Put all events into an array and sort. Sweep across line/plane and process events in order, update as events are processed.
If the number of types of events is small, can create multiple arrays for events and sort that instead.
Reducing the value of n.

Time Complexity:  O(n*log(n)) 

main bottleneck is the sorting (n is the number of events). 

Space Complexity:

O(n) for arrays to store the sorted events. 

Problems:

https://leetcode.com/problems/meeting-rooms-ii/
https://adventofcode.com/2025/day/5

### Find Top-k

### Boyer-Moore Majority Vote Algorithm
Find element with more than floor(n/2) occurrences amongst n elements.
Set the first element as the current candidate with a count of 1, whenever a different element is seen
decrement the count by 1, if the count is 0, change the candidate to the new element. If the element is the current
candidate, increment the count by 1. After iterating through all the elements, the candidate will be the majority element
if it exists.
To check if majority element exists, iterate through all elements and count occurrences of candidate, and check
if it has more than floor(n/2) occurrences, if its does its a majority element.

let i be the number of occurrences of the majority element in the array, then
the number of occurrences of other elements combined is j = n - i.
since i is the majority element, i > j. Since there are i increments for the majority element
and j decrements for the majority element, the candidate is guaranteed to be the majority element with count > 0 
after all elements are iterated through.

Time Complexity: O(n) 

Iterate through entire array, O(1) for each element.

Space Complexity: O(1)

Problems:

https://leetcode.com/problems/majority-element/
