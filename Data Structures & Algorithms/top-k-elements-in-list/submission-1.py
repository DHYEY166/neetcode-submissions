class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = []
        des = {}
        for i in range(len(nums)):
            des[nums[i]] = 1 + des.get(nums[i], 0)

        for i, j in des.items():
            a.append([j, i])
        a.sort()

        res = []
        while len(res) < k:
            res.append(a.pop()[1])
        return res
        

