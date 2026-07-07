class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #simple
        n = len(nums)
        a = [0] * (2*n)
        for i in range(n):
            a[i] = a[i+n] = nums[i]
        return a