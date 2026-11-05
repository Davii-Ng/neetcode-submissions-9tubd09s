class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)]

        for u, v, w in times:
            graph[u].append((v, w))

        dist = [float('inf')] * (n+1)
        dist[k] = 0


        heap = [(0 , k)]

        while heap:
            cost, node = heapq.heappop(heap)

            if cost > dist[node]:
                continue

            for neighbor, weight in graph[node]:
                new_dist = cost + weight
                if new_dist < dist[neighbor]:
                    heapq.heappush(heap, (new_dist, neighbor))
                    dist[neighbor] = new_dist

        ans = max(dist[1:])
        
        return ans if ans != float('inf') else -1