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
Usually to brute force problems.

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


### Power Set (Poset)
Get all possible subsets of n elements. This can be done via backtracking/dfs, iteratively (with bitmasking or none).
This can be done if the elements if the subset are unique or non unique.

Time Complexity: O(n*2^n)

For each element in the array, the decision to whether to include that element forms a full binary decision tree.
This is of depth n, hence has 2^n nodes. Each node takes O(n) to copy/store them.

Space Complexity: O(n) for recursion, if storing all subsets counted O(n * 2^n)

Problems:
https://leetcode.com/problems/subsets

https://leetcode.com/problems/subsets-ii

https://adventofcode.com/2025/day/10

## Searching

### Linear Search 
Checks every element in the search space.

Time Complexity: O(n)

Iterates over every element.

Space Complexity: O(1)

### Binary Search
Finds the target value by cutting the search space in half.

Conditions: 
1. Search space must be monotonically ordered (increasing or decreasing)


Time Complexity: O(log(n))

Search space reduces by half each iteration, each iteration takes O(1) time.
Recurrence relation will be T(n) = T(n/2) + O(1).
Solving this, T(n) = O(n)

Space Complexity: O(1)

Problems:

https://leetcode.com/problems/longest-increasing-subsequence
https://leetcode.com/problems/split-array-largest-sum/

### Ternary Search

### Quick Select
Finds the kth largest element in an array.

Time Complexity: 

Best/Average Case: O(n)

Search space reduced by on average half each iteration.

Recurrence Relation:
T(n) = T(n/2) + O(n) = O(n)

Worst Case: O(n^2), bad inputs.

### Newton's Method
Approximates roots of real valued function f(x) through updating the guess via an update function.
Repeat update process until converges to the root with desired tolerance.

Time Complexity: O(I*C) where C is the cost per iteration and I is the number of iterations.

Due to quadratic convergence, I Is approximately logarithmic with the number of correct digits.

Space Complexity: O(1)

## Sorting

### Bubble Sort
Swap adjacent elements such that the larger element is at the end. Every iteration, the largest element in the unsorted
portion will be pushed to the end. This sorting algorithm is stable.

Time Complexity: O(n^2)

Space Complexity: O(1)

### Selection Sort
Keep a subarray that is sorted, each iteration find the minimum element from the unsorted portion and swap it to the 
start of the start of the unsorted portion to expand the subarray. This sorting algorithm is not stable, as long as 
adjacent elements that are equal are not swapped

Time Complexity: O(n^2) 

Space Complexity: O(1)

### Insertion Sort
Keep a subarray at the start that is sorted, each iteration add one element to that subarray and keep it sorted.
This is done by continuously swapping adjacent elements until the new element is in position.
Stable and very fast on an almost sorted array. Stable as long as adjacent element that are equal are not swapped.

Time Complexity: 

Worst Case: O(n^2) 

Best Case: O(n) almost sorted array

Space Complexity: O(1)

### Merge Sort

Time Complexity: O(n*log(n))

Space Complexity: O(n)

### In-Place Merge Sort

Time Complexity: O(n*log^2(n))

Each merge takes O(n log n), and there are log(n) levels.

Hence the recurrence relation:

T(n) = 2T(n/2) + n*log(n) = O(n *log^2(n))

Space Complexity: O(1)

In place

### Quick Sort
Not stable sorting algorithm.

Time Complexity:

Best/Average Case: O(n*log(n))

Worst Case: O(n^2) Duplicates or bad inputs

Space Complexity: O(1)

### Randomised Quick Sort
Not stable sorting algorithm.

Time Complexity:

Expected: O(n*log(n))

Worst Case: O(n^2) Duplicates or luck

Space Complexity: O(1)

### Dual-Pivot Quick Sort

Time Complexity:

Expected: O(n*log(n))

Worst Case: O(n^2) For both randomised and not, removes vulnerability to duplicates

Space Complexity: O(1)

### Three-way Quick Sort
Not stable sorting algorithm.

Time Complexity:

Expected: O(n*log(n))

Worst Case: O(n^2) For both randomised and not, removes vulnerability to duplicates

Space Complexity: O(1)

### Bitonic Sort

### Bucket Sort

### Shell Sort

### Counting Sort
Counts the frequency of each element in an array, then makes a prefix sum array using the frequency array.
Position i in the prefix sum determines the index in the new array of element i. Iterate from the prefix
array from the back(to guarantee stability) and add elements to the new array and decrement the index stated at position i in the prefix array by 1 
each time to prevent the same element from overriding the in the new array.

Time Complexity: O(n + k), where k is the range of values and n is the number of values

To build the counting array, output array and iterating through all elements.

Space Complexity: O(n + k) 

For the counting array and the sorted array

### Radix Sort
Performs a stable counting sort on each digit of a base k number, starting from the lowest digit. 

Time Complexity: O(d(n + k)), where k is the base, n is the number of values and d is number of digits required (logk(largest value))

Space Complexity: O(n + k)

Uses counting sort, array is reused for each digit

## Trees

### Build Binary Tree From Array

### Pre Order Traversal (Binary Tree)

### In Order Traversal (Binary Tree)

### Post Order Traversal (Binary Tree)

### Vertex Cover

### Lowest Common Ancestor

## Dynamic Programming
Class of solutions where you can solve problems by breaking it into simpler subproblems recursively and solving them once and using the solution of the sub problems to solve the main problem.

DP works when 
1. Overlapping subproblems: The problem can be broken down into subproblems that repeat
2. Optimal substructure: The solution of the main problem can be constructed from the solutions of the sobproblems

Top-down DP is when you start from the main problem and recursively break down the problem and memoise the solution to not
solve it twice.

Bottom-up DP is when you solve the smallest subproblems first and use them to build up to the bigger sub problems and eventually the solution.

### 0/1 Knapsack
Given n items, each item has a weight and value associated with it(represented in an array). Find the maximum
possible value that can be derived with a max weight of W. 

Create a nxW dp array where dp[i][j] represents the maximum value using the first i items with capacity j
Iterate through each item, for each weight value up to the max weight(iterate backwards to prevent items from being counted twice). Fill in the dp array based on whether the ith item is taken or not, dp[i][j] = max(dp[i - 1][j - weight of i], dp[i - 1][j]). 

Time Complexity: O(n*W)

Space Complexity: O(W)

A 2D array to store all the values is unnecessary as only the previous row is necessary

Problems: 

https://leetcode.com/problems/partition-equal-subset-sum 

### Unbounded Knapsack
0/1 knapsack but you can take an unlimited number of items as long as the weight limit W is not exceeded.
When iterating through the max weight value, iterate forwards instead of backwards to allow for dupes to be counted.

Time Complexity: O(n*W)

Space Complexity: O(W)

A 2D array to store all the values is unnecessary as only the previous row is necessary

Problems:

https://leetcode.com/problems/coin-change-ii/

### Bounded Knapsack
0/1 knapsack but each item i has a maximum quantity that can be taken count[i].
if count[i] = 1 for every item, this reduces to 0/1 knapsack.

WIP: Power of two decomposition

## Graphs

### Is Tree
Checks if the graph is a tree. It is a tree iff it has n - 1 edges and the graph is fully connected.

### Find Number of Connected Components

### BFS

### DFS

### A-Star

### Kahn's Algorithm (Topological Sort)

### Topological Sort DFS

### Prim's Algorithm
For a weighted graph, finds minimum spanning tree. 

From a starting vertex, for each iteration, add the cheapest edge that connects the tree to a new vertex.
Stop when all vertices are included.

Time Complexity: 

O(E log(V)) for adj list + binary heap

O(E + Vlog(V)) for adj list + fibonacci heap (better for sparse graphs)

O(V^2) for adj matrix

Space Complexity:

O(V + E) for adj list

O(V^2) for adj matrix
 
Problems:

https://leetcode.com/problems/connecting-cities-with-minimum-cost

### Kruskal's Algorithm 
For a weighted graph, finds minimum spanning tree.

Sorts edges by weight and unions the edges one by one(if both are from different groups) until V - 1 are processed(its a tree).
 
Time Complexity: O(E log(E)) 

Sorting the edges bottlenecks the time complexity.

Space Complexity: O(V + E) for adj list

Problems:

https://leetcode.com/problems/connecting-cities-with-minimum-cost


### Dijkstra's Algorithm
Finds the shortest path from single source to all other vertices in a graph with non-negative edge weights.

Time Complexity:

O((V + E)*log(V)) Binary heap + adj list

O(E + V*log(V)) Fibonacci heap + adj list (for sparse graphs)

O(E*log(V)) Binary heap + adj list (no decrease key in python heapq so put every edge inside)

O(V^2) Array/Adj matrix

Problems:

https://leetcode.com/problems/network-delay-time/

### Bellman Ford
Finds the shortest path from single source to all other vertices in a graph with non-negative edge weights.

Run relaxation on every edge V - 1 times. Only works if no negative cycles. Run relaxation on edge one more time, if any distances improve, a negative cycle exists.

Problems:

Time Complexity: O(VE)

Run O(1) relaxation on E edges V times.

Space Complexity: 

O(V + E)

O(V) if edge list is not counted

https://leetcode.com/problems/network-delay-time/


### Floyd Warshall
Gets shortest distance between all pairs of vertices in a weighted graph.

dp[i][j] represents the shortest path from i to j using intermediates <= k.
Iterate over all k, i, j in order to build the dp array.

If any distance between any pair of nodes is < 0, a negative cycle exists.

Time Complexity: O(V^3)

Space Complexity: O(V^2)

Problems:

https://leetcode.com/problems/network-delay-time/

https://leetcode.com/problems/cheapest-flights-within-k-stops/

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
If the number of types of events is small, can create multiple arrays for events and sort that instead to reduce
amount of computation.

Time Complexity:  O(n*log(n)) 

main bottleneck is the sorting (n is the number of events). 

Space Complexity: O(n)

For arrays to store the sorted events. 

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
