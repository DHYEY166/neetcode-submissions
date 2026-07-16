class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #optimised

        res = []
        for i in nums:
            if i not in res:
                res.append(i)

            else:
                return True
        return False
                