class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        area = 0

        visited = set()

        directions = [(1,0), (-1,0), (0, 1), (0,-1)]

        def dfs(r, c):
            visited.add((r,c))
            temp = 1
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited and grid[nr][nc] == 1:

                    temp += dfs(nr, nc)

            return temp



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] and (r,c) not in visited:
                    area = max(dfs(r, c), area)
        return area
