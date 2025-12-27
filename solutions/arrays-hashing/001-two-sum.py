"""
LeetCode 1: Two Sum
===================
Difficulty: Easy
Pattern: Arrays & Hashing
Date Solved: YYYY-MM-DD

Problem:
Given an array of integers nums and an integer target, return indices 
of the two numbers such that they add up to target.

Key Insight:
Use a hash map to store each number's index as we iterate. For each number,
check if its complement (target - num) exists in the map.

Time Complexity: O(n) - single pass through array
Space Complexity: O(n) - hash map stores up to n elements
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map: value -> index
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if complement already seen
            if complement in seen:
                return [seen[complement], i]
            
            # Store current number's index
            seen[num] = i
        
        # No solution found (problem guarantees one exists)
        return []


# =============================================================================
# ALTERNATIVE APPROACHES
# =============================================================================

class BruteForce:
    """
    Time: O(n²) - check every pair
    Space: O(1)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


class SortedTwoPointers:
    """
    Time: O(n log n) - sorting dominates
    Space: O(n) - need to store original indices
    
    Note: This approach loses original indices, so we need to track them.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Store (value, original_index) pairs
        indexed = [(num, i) for i, num in enumerate(nums)]
        indexed.sort()
        
        left, right = 0, len(indexed) - 1
        
        while left < right:
            current_sum = indexed[left][0] + indexed[right][0]
            
            if current_sum == target:
                return [indexed[left][1], indexed[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        return []


# =============================================================================
# TEST CASES
# =============================================================================

if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Basic case
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    
    # Test case 2: Target in middle
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    
    # Test case 3: Same number twice
    assert solution.twoSum([3, 3], 6) == [0, 1]
    
    # Test case 4: Negative numbers
    assert solution.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]
    
    print("All test cases passed!")


# =============================================================================
# NOTES & LEARNINGS
# =============================================================================
"""
What I learned:
1. Hash maps turn O(n) lookup into O(1)
2. The "complement" pattern is very common
3. Always consider what to store in the hash map (value vs index)

Related problems:
- Two Sum II (sorted array - use two pointers)
- 3Sum (sort + two pointers)
- 4Sum (sort + recursion + two pointers)

Edge cases to remember:
- Duplicate values
- Negative numbers
- Single valid pair vs multiple pairs
"""
