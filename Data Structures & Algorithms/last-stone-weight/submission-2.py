class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)


        while len(heap) > 1:
            one, two  = -heapq.heappop(heap), -heapq.heappop(heap)
            start = abs(two - one)
            heapq.heappush(heap, -start)

        return -heap[0] if heap else 0