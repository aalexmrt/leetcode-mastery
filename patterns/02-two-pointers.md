# Two Pointers

## Overview

The two pointers technique uses two indices to traverse an array or string, typically moving towards each other or in the same direction. It transforms O(n²) brute force into O(n) solutions.

## When to Use

- Sorted array + looking for pairs
- Palindrome checking
- Removing duplicates in-place
- Merging sorted arrays
- Container/area problems
- Finding triplets/quadruplets

## Types of Two Pointers

### 1. Opposite Direction (Converging)
Pointers start at ends, move toward center.

```python
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1  # need larger sum
        else:
            right -= 1  # need smaller sum
    
    return []
```

### 2. Same Direction (Fast/Slow)
Both pointers move forward, at different speeds.

```python
def remove_duplicates(nums):
    if not nums:
        return 0
    
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    
    return slow + 1
```

### 3. Sliding Window Variant
One pointer defines start, other defines end of window.
(See Sliding Window pattern for details)

## Key Techniques

### Palindrome Check
```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True
```

### 3Sum (Using Two Pointers inside loop)
```python
def three_sum(nums):
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        # Skip duplicates for first element
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        target = -nums[i]
        
        while left < right:
            current = nums[left] + nums[right]
            if current == target:
                result.append([nums[i], nums[left], nums[right]])
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif current < target:
                left += 1
            else:
                right -= 1
    
    return result
```

### Container With Most Water
```python
def max_area(height):
    left, right = 0, len(height) - 1
    max_water = 0
    
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_water = max(max_water, width * h)
        
        # Move the shorter line (greedy)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water
```

## Common Patterns

| Problem Type | Pointer Setup | Movement Logic |
|-------------|---------------|----------------|
| Pair with target sum | Opposite ends | Sum too small → left++, too big → right-- |
| Palindrome | Opposite ends | Compare, move both inward |
| Remove duplicates | Same direction | Slow marks position, fast scans |
| Merge sorted | Same direction | Compare heads, advance smaller |
| Container area | Opposite ends | Move shorter side |

## Problems in This Category

| # | Problem | Difficulty | Key Insight |
|---|---------|------------|-------------|
| 125 | Valid Palindrome | Easy | Skip non-alphanumeric, compare ends |
| 167 | Two Sum II | Medium | Sorted array → opposite pointers |
| 15 | 3Sum | Medium | Sort + fix one, two-pointer for rest |
| 11 | Container With Most Water | Medium | Greedy: move shorter line |
| 42 | Trapping Rain Water | Hard | Track left_max and right_max |

## Common Mistakes

1. **Forgetting to sort** when the technique requires sorted input
2. **Infinite loops**: forgetting to move pointers
3. **Off-by-one**: using `<=` vs `<` in while condition
4. **Duplicate handling**: not skipping duplicates in 3Sum-style problems
5. **Wrong pointer to move**: in converging problems, logic for which pointer matters

## Template

```python
"""
Problem: [Name]
Pattern: Two Pointers
Time: O(n) or O(n²) for nested
Space: O(1) typically
"""

def solve(nums):
    # Possibly sort first
    nums.sort()  # if needed
    
    left, right = 0, len(nums) - 1
    result = initial_value
    
    while left < right:
        current = calculate(nums[left], nums[right])
        
        if meets_condition(current):
            update_result()
            # Move both or one pointer
        elif need_larger:
            left += 1
        else:
            right -= 1
    
    return result
```

## Related Patterns

- **Sliding Window**: When window size varies based on condition
- **Binary Search**: When you can eliminate half the search space
- **Fast/Slow Pointers**: Specifically for linked list cycle detection
