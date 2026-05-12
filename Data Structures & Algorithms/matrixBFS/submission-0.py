class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque([(0,0)])
        visit = {(0,0)}

        def check_directions(q, r, c, visit):
            dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for dr, dc in dir:
                nr, nc = r + dr, c + dc
                #Check boundaries
                if nr < 0 or nc <0 or nr >= rows or nc >= cols:
                    continue
                #blocked or visited
                if (nr,nc) in visit or grid[nr][nc] == 1:
                    continue

                q.append((nr, nc))
                visit.add((nr, nc))

        length = 0
        while q:
            for i in range(len(q)):
                #pop this level
                r, c = q.popleft()

                if (r,c) == (rows - 1, cols - 1):
                    return length

                check_directions(q, r, c, visit)
            
            length += 1
        
        return -1
            