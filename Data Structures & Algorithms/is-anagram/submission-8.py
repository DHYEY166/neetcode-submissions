class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # first approach
        s, t = sorted(s), sorted(t)
        return s == t