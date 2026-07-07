class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # first approach
        if len(s) != len(t):
            return False

        s, t = sorted(s), sorted(t)
        return s == t