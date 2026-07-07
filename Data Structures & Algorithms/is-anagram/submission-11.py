class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # second approach
        if len(s) != len(t):
            return False

        see_s, see_t = {}, {}
        for i in range(len(s)):
            see_s[s[i]] = 1 + see_s.get(s[i], 0)
            see_t[t[i]] = 1 + see_t.get(t[i], 0)
        return see_s == see_t