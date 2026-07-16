class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #simple
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)