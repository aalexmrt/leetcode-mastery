# Sliding Window

## Overview

Sliding window maintains a "window" over a contiguous portion of an array or string, expanding and contracting to find optimal subarrays/substrings. It reduces O(n²) brute force to O(n).

## When to Use

- Problems involving **contiguous** subarrays or substrings
- Finding min/max length subarray with a constraint
- Problems with keywords: "subarray", "substring", "contiguous", "consecutive"
- When asked about "longest", "shortest", "maximum sum" of contiguous elements

## Types of Sliding Window

### 1. Fixed Size Window
Window size is given, slide it across.

```python
def max_sum_subarray_k(nums, k):
    # Initial window
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]  # Add right, remove left
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

### 2. Variable Size Window (Expand/Contract)
Window size changes based on constraints.

```python
def longest_substring_k_distinct(s, k):
    char_count = {}
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # Expand: add right character
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # Contract: while constraint violated
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        # Update result
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

## Key Techniques

### Longest Substring Without Repeating Characters
```python
def length_of_longest_substring(s):
    char_index = {}  # char -> last seen index
    left = 0
    max_length = 0
    
    for right, char in enumerate(s):
        # If char seen and within current window
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1  # Move left past duplicate
        
        char_index[char] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

### Minimum Window Substring
```python
from collections import Counter

def min_window(s, t):
    if not t or not s:
        return ""
    
    target_count = Counter(t)
    required = len(target_count)
    
    left = 0
    formed = 0
    window_count = {}
    result = (float('inf'), 0, 0)  # (length, left, right)
    
    for right, char in enumerate(s):
        # Expand
        window_count[char] = window_count.get(char, 0) + 1
        
        if char in target_count and window_count[char] == target_count[char]:
            formed += 1
        
        # Contract while valid
        while formed == required:
            if right - left + 1 < result[0]:
                result = (right - left + 1, left, right)
            
            # Remove left char
            left_char = s[left]
            window_count[left_char] -= 1
            if left_char in target_count and window_count[left_char] < target_count[left_char]:
                formed -= 1
            left += 1
    
    return "" if result[0] == float('inf') else s[result[1]:result[2] + 1]
```

### Maximum Sum Subarray of Size K
```python
def max_sum_k(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    for i in range(k, len(nums)):
        window_sum = window_sum + nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

## Common Patterns

| Problem Type | Window Type | Key Data Structure |
|-------------|-------------|-------------------|
| Max sum of size k | Fixed | Running sum |
| Longest with ≤k distinct | Variable | Hash map (char count) |
| Smallest with sum ≥ target | Variable | Running sum |
| Contains all chars of t | Variable | Two hash maps |
| Max consecutive 1s with k flips | Variable | Count of zeros |

## Problems in This Category

| # | Problem | Difficulty | Key Insight |
|---|---------|------------|-------------|
| 121 | Best Time to Buy/Sell Stock | Easy | Track min price, max profit |
| 3 | Longest Substring No Repeat | Medium | Hash map for last index |
| 424 | Longest Repeating Char Replace | Medium | Window - max_freq ≤ k |
| 567 | Permutation in String | Medium | Fixed window, char count match |
| 76 | Minimum Window Substring | Hard | Expand until valid, contract |
| 239 | Sliding Window Maximum | Hard | Monotonic deque |

## Common Mistakes

1. **Off-by-one in window size**: `right - left + 1` vs `right - left`
2. **Forgetting to update result**: Check result update timing (after expand? after contract?)
3. **Not handling empty input**
4. **Wrong contraction condition**: `while` vs `if`
5. **Incorrect character count update**: Increment/decrement at wrong time

## Template

```python
"""
Problem: [Name]
Pattern: Sliding Window
Time: O(n)
Space: O(k) where k is character set size
"""

def solve(s):
    left = 0
    result = initial_value
    window_state = {}  # or counter, sum, etc.
    
    for right in range(len(s)):
        # 1. Expand: add s[right] to window
        update_window_state(s[right])
        
        # 2. Contract: while window invalid
        while window_invalid():
            remove_from_window(s[left])
            left += 1
        
        # 3. Update result (may be inside or outside while loop)
        result = update_result(result, right - left + 1)
    
    return result
```

## When to Update Result

- **Finding maximum**: Update after expanding (window might be valid)
- **Finding minimum**: Update while contracting (looking for smallest valid)
- **Finding exact match**: Update when condition exactly met

## Related Patterns

- **Two Pointers**: Sliding window is a special case
- **Prefix Sum**: Alternative for sum-based problems
- **Monotonic Queue/Stack**: For sliding window maximum/minimum
