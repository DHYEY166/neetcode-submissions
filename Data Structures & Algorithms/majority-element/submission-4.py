class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #second solution
        a = {}
        for i in range(len(nums)):
            a[nums[i]] = 1 + a.get(nums[i], 0)
        
        for k, v in a.items():
            if v > len(nums) // 2:
                return k
        return []
