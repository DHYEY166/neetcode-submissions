class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heapq.heapify(nums)
        target = n - k
        while target > 0:
            heapq.heappop(nums)
            target -= 1

        return nums[0]
