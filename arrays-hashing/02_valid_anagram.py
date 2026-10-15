"""
Problem: Valid Anagram (Blind 75 / NeetCode 150)
Pattern: Anagram
Anagram means two strings with same characters
Check lenght and if pass sort to verify
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

 if __name__ == "__main__":
   sol = Solution()
   assert sol.isAnagram("racecar", "carrace") is True
   assert sol.isAnagram("Miami", "Madrid") is False
   print("All test cases passed succesfully")
