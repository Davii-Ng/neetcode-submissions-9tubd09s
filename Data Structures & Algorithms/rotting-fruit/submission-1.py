class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        BFS approach 

        The number of rotten 
        The number of fresh

        Every minute = One iteration in the queue
        increment the no.rotten

        return if rott = fresh else -1
        """
        
        rotten = 0
        fresh = 0

        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        visited = set()

        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))



        minutes = 0
        
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        fresh -= 1
                        grid[nr][nc] = 2

            minutes += 1


        return minutes  if fresh == 0 else -1


        