"""
Scratch pad for working on LeetCode problems.
Run with: python scratch.py
"""

from typing import List


# =============================================================================
# CURRENT PROBLEM: Contains Duplicate (LeetCode 217)
# =============================================================================
"""
Given an integer array nums, return true if any value appears at least twice,
and false if every element is distinct.

Example 1: nums = [1, 2, 3, 1] → true
Example 2: nums = [1, 2, 3, 4] → false
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
          

   


# =============================================================================
# TEST YOUR SOLUTION
# =============================================================================
if __name__ == "__main__":
    s = Solution()

    print("Test 1:", s.containsDuplicate([1, 2, 3, 1]))        # Expected: True
    print("Test 2:", s.containsDuplicate([1, 2, 3, 4]))        # Expected: False
    print("Test 3:", s.containsDuplicate([1, 1, 1, 3, 3, 4]))  # Expected: True
    print("Test 4:", s.containsDuplicate([]))                   # Expected: False
    print("Test 5:", s.containsDuplicate([1]))                  # Expected: False
