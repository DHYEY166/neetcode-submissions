class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        des = {}
        for n in nums:
            des[n] = 1 + des.get(n, 0)
        
        arr = []
        for value, index in des.items():
            arr.append([index, value])
        arr.sort()
        
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res



