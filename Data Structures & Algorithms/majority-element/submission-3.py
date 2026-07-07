class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #single line
        nums.sort()
        return nums[len(nums) // 2]