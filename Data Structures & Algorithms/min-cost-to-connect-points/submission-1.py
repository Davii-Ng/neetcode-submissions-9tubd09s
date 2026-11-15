class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #Prim
        """
        Go through eahch points, if push into heap pop heap, if element not in visited sum up
        """

        heap = []
        visited = set()

        total = 0

        n = len(points)

        adj = defaultdict(list)

        #Adjacency list
        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                
                xj, yj = points[j]

                dist = abs(xi-xj) + abs(yj-yi)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        
        res = 0
        minH = [[0,0]]

        while len(visited) < n:
            cost, i = heapq.heappop(minH)
            if i in visited:
                continue

            res += cost
            visited.add(i)
            for dist, nei in adj[i]:
                if nei not in visited:
                    heapq.heappush(minH, [dist, nei])

        return res


                
                


            