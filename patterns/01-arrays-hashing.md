# Arrays & Hashing

## Overview

Arrays and hash maps are foundational data structures. This pattern focuses on using **hash maps (dictionaries)** to achieve O(1) lookups, enabling efficient solutions to problems that would otherwise require O(n²) brute force.

## When to Use

- Need to check if an element exists → Hash Set
- Need to count frequencies → Hash Map
- Need to find pairs/complements → Hash Map (store value → index)
- Need to group elements → Hash Map (key → list)
- Need O(1) lookup instead of O(n) search

## Key Techniques

### 1. Frequency Counting
```python
from collections import Counter

def count_frequencies(nums):
    freq = Counter(nums)  # or {}; for n in nums: freq[n] = freq.get(n, 0) + 1
    return freq
```

### 2. Complement Lookup (Two Sum Pattern)
```python
def two_sum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

### 3. Grouping by Key
```python
from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))  # or use character count as key
        groups[key].append(s)
    return list(groups.values())
```

### 4. Using Sets for Existence Checks
```python
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
    # Or simply: return len(nums) != len(set(nums))
```

## Common Patterns

| Problem Type | Approach | Time | Space |
|-------------|----------|------|-------|
| Find duplicates | Set | O(n) | O(n) |
| Two Sum | Hash map (val → idx) | O(n) | O(n) |
| Frequency count | Counter / dict | O(n) | O(n) |
| Group by property | defaultdict(list) | O(n) | O(n) |
| Check anagram | Sorted comparison or Counter | O(n log n) or O(n) | O(n) |

## Problems in This Category

| # | Problem | Difficulty | Key Insight |
|---|---------|------------|-------------|
| 217 | Contains Duplicate | Easy | Set for O(1) lookup |
| 242 | Valid Anagram | Easy | Character frequency comparison |
| 1 | Two Sum | Easy | Hash map for complement lookup |
| 49 | Group Anagrams | Medium | Sorted string as grouping key |
| 347 | Top K Frequent Elements | Medium | Counter + heap or bucket sort |
| 238 | Product of Array Except Self | Medium | Prefix and suffix products |
| 36 | Valid Sudoku | Medium | Sets for rows, cols, boxes |
| 271 | Encode and Decode Strings | Medium | Length-prefix encoding |
| 128 | Longest Consecutive Sequence | Medium | Set + expand from sequence starts |

## Common Mistakes

1. **Forgetting to handle empty input**
2. **Off-by-one errors with indices**
3. **Mutating the input array when you shouldn't**
4. **Using list instead of set for lookups** (O(n) vs O(1))
5. **Not considering negative numbers or zeros**

## Template

```python
"""
Problem: [Name]
Pattern: Arrays & Hashing
Time: O(n)
Space: O(n)
"""

def solve(nums):
    # 1. Initialize hash map/set
    seen = {}
    
    # 2. Single pass through array
    for i, num in enumerate(nums):
        # 3. Check condition using hash map
        if condition_met(num, seen):
            return result
        
        # 4. Update hash map
        seen[num] = i  # or relevant value
    
    return default_result
```

## Related Patterns

- **Two Pointers**: Often an alternative when array is sorted
- **Sliding Window**: When dealing with contiguous subarrays
- **Prefix Sum**: When dealing with subarray sums
