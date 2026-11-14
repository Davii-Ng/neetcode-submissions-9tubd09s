class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        
        return x

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

        if self.size[root_b] < self.size[root_a]:
            root_a, root_b = root_b, root_a
        
        self.parent[root_b] = root_a
        self.size[root_a] += root_b  

        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dsu = DSU(n)
        total = 0
        edges = []

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                edges.append((dist, i, j))

        edges.sort()
        
        for dist, u, v in edges:
            if dsu.union(u, v):
                total += dist
        
        return total


