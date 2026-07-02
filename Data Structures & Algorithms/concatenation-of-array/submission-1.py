class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        a = []
        for i in range(2):
            for n in nums:
                a.append(n)
        return a
