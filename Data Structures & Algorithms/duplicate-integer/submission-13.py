class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # third approach
        a = {}
        for i in range(len(nums)):
            a[nums[i]] = 1 + a.get(nums[i], 0)
        
        for v in a.values():
            if v != 1:
                return True
        return False