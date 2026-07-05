class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #optimised
        nums.sort()
        return nums[len(nums) // 2]