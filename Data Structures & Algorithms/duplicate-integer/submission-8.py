class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #optimised
        seet = set()
        for i in nums:
            if i in seet:
                return True
            seet.add(i)

        return False