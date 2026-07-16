class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        des = {}
        for n in nums:
            des[n] = 1 + des.get(n, 0)

        heap = []
        for num in des.keys():
            heapq.heappush(heap, (des[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res


        



