class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if not nums:
            return False

        a = []
        a.append(nums[0])
        for i in nums[1:]:
            if i in a:
                return True
            else:
                a.append(i)
        return False
