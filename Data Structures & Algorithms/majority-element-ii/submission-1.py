class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a = {}
        res = []
        for i in range(len(nums)):
            a[nums[i]] = 1 + a.get(nums[i], 0)

        for k, v in a.items():
            if v > len(nums) // 3:
                res.append(k)
        
        return res
