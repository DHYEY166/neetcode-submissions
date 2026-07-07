class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #scalable
        a = []
        for i in range(2):
            for i in range(len(nums)):
                a.append(nums[i])
        return a