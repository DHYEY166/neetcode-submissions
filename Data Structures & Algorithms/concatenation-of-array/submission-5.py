class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #optimised
        n = len(nums)
        ans = [0] * (2*n)
        for index, num in enumerate(nums):
            ans[index] = ans[index+n] = num
        return ans