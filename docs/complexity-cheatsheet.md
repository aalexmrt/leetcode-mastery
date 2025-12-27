# Complexity Cheat Sheet

## Big-O Quick Reference

### Time Complexity (Best to Worst)

| Notation | Name | Example |
|----------|------|---------|
| O(1) | Constant | Hash table lookup, array index access |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Single loop, linear search |
| O(n log n) | Linearithmic | Efficient sorting (merge, quick, heap) |
| O(n²) | Quadratic | Nested loops, bubble sort |
| O(n³) | Cubic | Triple nested loops |
| O(2ⁿ) | Exponential | Recursive Fibonacci, subsets |
| O(n!) | Factorial | Permutations |

### For n = 1,000,000

| Complexity | Operations | Feasible? |
|------------|------------|-----------|
| O(1) | 1 | ✅ Instant |
| O(log n) | 20 | ✅ Instant |
| O(n) | 1,000,000 | ✅ ~1 second |
| O(n log n) | 20,000,000 | ✅ ~few seconds |
| O(n²) | 10¹² | ❌ Too slow |
| O(2ⁿ) | Astronomical | ❌ Impossible |

## Common Data Structure Operations

### Array / List

| Operation | Time |
|-----------|------|
| Access by index | O(1) |
| Search (unsorted) | O(n) |
| Search (sorted) | O(log n) |
| Insert at end | O(1) amortized |
| Insert at middle | O(n) |
| Delete | O(n) |

### Hash Table / Dictionary

| Operation | Average | Worst |
|-----------|---------|-------|
| Insert | O(1) | O(n) |
| Delete | O(1) | O(n) |
| Search | O(1) | O(n) |

### Linked List

| Operation | Time |
|-----------|------|
| Access by index | O(n) |
| Insert at head | O(1) |
| Insert at tail (with pointer) | O(1) |
| Insert at middle | O(n) |
| Delete | O(n) |

### Stack / Queue

| Operation | Time |
|-----------|------|
| Push / Enqueue | O(1) |
| Pop / Dequeue | O(1) |
| Peek | O(1) |

### Binary Search Tree (Balanced)

| Operation | Average | Worst (unbalanced) |
|-----------|---------|-------------------|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |

### Heap / Priority Queue

| Operation | Time |
|-----------|------|
| Insert | O(log n) |
| Extract min/max | O(log n) |
| Peek min/max | O(1) |
| Build heap | O(n) |

### Trie

| Operation | Time |
|-----------|------|
| Insert | O(m) where m = word length |
| Search | O(m) |
| Delete | O(m) |

## Common Algorithm Complexities

### Sorting

| Algorithm | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) |
| Tim Sort (Python) | O(n) | O(n log n) | O(n log n) | O(n) |
| Counting Sort | O(n + k) | O(n + k) | O(n + k) | O(k) |

### Graph Algorithms

| Algorithm | Time | Space |
|-----------|------|-------|
| BFS | O(V + E) | O(V) |
| DFS | O(V + E) | O(V) |
| Dijkstra (binary heap) | O((V + E) log V) | O(V) |
| Bellman-Ford | O(V × E) | O(V) |
| Floyd-Warshall | O(V³) | O(V²) |
| Topological Sort | O(V + E) | O(V) |
| Union-Find | O(α(n)) ≈ O(1) | O(n) |

### Dynamic Programming

| Problem Type | Time | Space |
|--------------|------|-------|
| Fibonacci | O(n) | O(1) optimized |
| LCS | O(m × n) | O(m × n) or O(min(m,n)) |
| Knapsack | O(n × W) | O(n × W) or O(W) |
| Edit Distance | O(m × n) | O(m × n) or O(min(m,n)) |

## Space Complexity Patterns

| Pattern | Typical Space |
|---------|---------------|
| Two pointers | O(1) |
| Sliding window | O(1) to O(k) |
| Hash map | O(n) |
| Recursion | O(depth) stack |
| BFS | O(width of level) |
| DFS | O(depth) |
| DP table | O(n) or O(n²) |
| Memoization | O(unique states) |

## Quick Rules of Thumb

1. **Nested loops**: Multiply complexities
   - Two nested loops over n → O(n²)
   - Loop within binary search → O(n log n)

2. **Recursion**: 
   - T(n) = T(n-1) + O(1) → O(n)
   - T(n) = 2T(n/2) + O(n) → O(n log n) (merge sort)
   - T(n) = 2T(n-1) + O(1) → O(2ⁿ) (naive Fibonacci)

3. **When to use what**:
   - O(1) lookup needed? → Hash table
   - Sorted data + search? → Binary search
   - Finding k-th element? → Heap or quickselect
   - All pairs/combinations? → At least O(n²)
   - All subsets? → O(2ⁿ)
   - All permutations? → O(n!)

4. **Amortized analysis**:
   - Dynamic array append: O(1) amortized
   - Union-Find with path compression: O(α(n)) ≈ O(1)

## Interview Tip

When asked about complexity:
1. State time complexity first
2. State space complexity second
3. Briefly justify ("We visit each element once, so O(n)")
4. Mention if it's amortized when applicable
