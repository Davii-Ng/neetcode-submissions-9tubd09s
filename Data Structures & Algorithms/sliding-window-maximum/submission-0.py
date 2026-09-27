class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = [(-nums[i], i) for i in range(k)]
        heapq.heapify(heap)
        ans = [-heap[0][0]]

        for i in range(k, len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            while heap[0][1] <= i - k:      # top left the window
                heapq.heappop(heap)
            ans.append(-heap[0][0])

        return ans


