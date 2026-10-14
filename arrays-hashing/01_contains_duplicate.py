"""
Problem: Contains Duplicate (Blind 75 / NeetCode 150)
Pattern: Arrays & Hashing
Time Complexity:  O(N) - single pass hash lookup
Space Complexity: O(N) - set memory buffer
"""

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

if __name__ == "__main__":
    sol = Solution()
    assert sol.hasDuplicate([1, 2, 3, 3]) is True
    assert sol.hasDuplicate([1, 2, 3, 4]) is False
    print("All test cases passed successfully.")
