class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        area = 0

        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        
        def bfs(r,c):
            q = collections.deque()
            
            
            q.append((r,c))
            visited.add((r,c))
            area = 1
            

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr,nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        area += 1

            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = max(area, bfs(r,c))

        return area




