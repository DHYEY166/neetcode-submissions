class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # second approach
        a = set()
        for num in nums:
            a.add(num)
        if len(a) < len(nums):
            return True
        else:
            return False