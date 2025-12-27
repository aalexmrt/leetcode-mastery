"""
Scratch pad for working on LeetCode problems.
Run with: python scratch.py
"""

from typing import List


# =============================================================================
# CURRENT PROBLEM: Two Sum (LeetCode 1)
# =============================================================================
"""
Given an array of integers nums and an integer target, return indices
of the two numbers such that they add up to target.

Example: nums = [2, 7, 11, 15], target = 9 → [0, 1]
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for x in range(len(nums)):
            num = nums[x]
            # print(num, 'num')
            complement = target - num;
            # print(complement, 'complement')
            if complement in seen:
                # print(seen.get(complement), 'seen')
                return [seen[complement], x]
            seen[num] = x
            # print(seen)
         
           

     


# =============================================================================
# TEST YOUR SOLUTION
# =============================================================================
if __name__ == "__main__":
    s = Solution()

    # Test cases
    print("Test 1:", s.twoSum([2, 7, 11, 15], 9))  # Expected: [0, 1] (adjacent)
    print("Test 2:", s.twoSum([3, 2, 4], 6))       # Expected: [1, 2] (adjacent)
    print("Test 3:", s.twoSum([3, 3], 6))          # Expected: [0, 1] (adjacent)

    # Non-adjacent pairs (your current solution will fail these)
    print("Test 4:", s.twoSum([1, 5, 3, 4], 8))    # Expected: [1, 2] → 5 + 3
    print("Test 5:", s.twoSum([2, 4, 5, 1], 3))    # Expected: [0, 3] → 2 + 1
    print("Test 6:", s.twoSum([1, 2, 3, 4, 5], 9)) # Expected: [3, 4] → 4 + 5
