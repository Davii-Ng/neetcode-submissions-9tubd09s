class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def _calc_euclidean(x, y):
            return x**2 + y**2


        heap = []
        for point in points:
            bundle = (-_calc_euclidean(point[0], point[1]), point)
            heapq.heappush(heap, bundle)
            if len(heap) > k:
                heapq.heappop(heap)

        ans = []

        for bundle in heap:
            ans.append(bundle[1])

        return ans