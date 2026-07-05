class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #optimised
        des = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in des:
                return [des[diff], i]
            des[n] = i
        return []