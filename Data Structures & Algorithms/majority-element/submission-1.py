class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        dct = {}
        n = len(nums)

        for num in nums:
            dct[num] = 1 + dct.get(num, 0)
            if dct[num] > n//2:
                return num