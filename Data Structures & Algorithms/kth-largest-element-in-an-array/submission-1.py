class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        target = len(nums) - k
        while target > 0:
            heapq.heappop(nums)
            target -= 1

        return nums[0]
