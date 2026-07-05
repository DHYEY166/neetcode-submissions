class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #optimised
        des = {}
        for i, n in enumerate(nums):
            left = target - n
            if left in des:
                return [des[left], i]
            des[n] = i
        return []