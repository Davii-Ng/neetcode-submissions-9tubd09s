class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        pac = [[False] * COLS for _ in range(ROWS)]
        atl = [[False] * COLS for _ in range(ROWS)]

        pacific = []
        atlantic = []

        directions = [(1,0), (-1,0), (0, 1), (0, -1)]

        for c in range(COLS):
            pacific.append((0, c))
            atlantic.append((ROWS - 1, c))

        for r in range(ROWS):
            pacific.append((r, 0))
            atlantic.append((r, COLS - 1))

        def BFS(source, ocean):
            q = deque()

            for (r, c) in source:
                if not ocean[r][c]:
                    q.append((r,c))
                    ocean[r][c] = True

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and not ocean[nr][nc] and heights[nr][nc] >= heights[r][c]:
                        ocean[nr][nc] = True
                        q.append((nr, nc))

        BFS(pacific, pac)
        BFS(atlantic, atl)

        ans = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    ans.append([r, c])


        return ans

        