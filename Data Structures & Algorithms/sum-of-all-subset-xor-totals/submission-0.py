class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i, total):
            if i == len(nums):
                return total # ^ SYMBOL FOR XOR
            return dfs(i + 1, total ^ nums[i]) + dfs(i + 1, total) 
            # adding both, INCLUDE NUMBER OR NOT INCLUDE NUMBER, SO 2 def()

        return dfs(0, 0)