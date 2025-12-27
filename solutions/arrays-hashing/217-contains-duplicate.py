"""
LeetCode 217: Contains Duplicate
================================
Difficulty: Easy
Pattern: Arrays & Hashing
Date Solved: 2025-12-27

Problem:
Given an integer array nums, return true if any value appears at least twice,
and false if every element is distinct.

Key Insight:
Use a set to track seen numbers. Sets have O(1) lookup, so we can check for
duplicates as we iterate through the array.

Time Complexity: O(n) - single pass through array
Space Complexity: O(n) - set stores up to n elements

Mistake Made:
Initially used dict syntax `seen[num] = True` on a set. Sets use `.add()` method,
not item assignment. Remember: sets store values, dicts store key-value pairs.
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False


# =============================================================================
# ALTERNATIVE APPROACHES
# =============================================================================

class SetLength:
    """
    Time: O(n) - set construction
    Space: O(n) - set of all elements

    One-liner: if set removes duplicates, lengths will differ.
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


class Sorting:
    """
    Time: O(n log n) - sorting dominates
    Space: O(1) or O(n) - depends on sort implementation

    After sorting, duplicates are adjacent.
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True

        return False


# =============================================================================
# TEST CASES
# =============================================================================

if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Has duplicate
    assert solution.containsDuplicate([1, 2, 3, 1]) == True

    # Test case 2: All unique
    assert solution.containsDuplicate([1, 2, 3, 4]) == False

    # Test case 3: Multiple duplicates
    assert solution.containsDuplicate([1, 1, 1, 3, 3, 4]) == True

    # Test case 4: Empty array
    assert solution.containsDuplicate([]) == False

    # Test case 5: Single element
    assert solution.containsDuplicate([1]) == False

    print("All test cases passed!")


# =============================================================================
# NOTES & LEARNINGS
# =============================================================================
"""
What I learned:
1. Sets use .add() method, not dict-style assignment
2. Set lookup is O(1), making it ideal for duplicate detection
3. The one-liner len(nums) != len(set(nums)) is elegant but less efficient
   for early termination (always processes entire array)

Related problems:
- Contains Duplicate II (check duplicates within k distance)
- Contains Duplicate III (check duplicates within k distance and value diff)

Edge cases to remember:
- Empty array (return False)
- Single element (return False)
- All duplicates
"""
