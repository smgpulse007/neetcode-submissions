class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        #if start is blocked
        if grid[0][0] == 1:
            return 0
        
        def dfs(grid, r, c, visited):
            #Boundary Condition
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return 0  
            # Check visited or blocked
            if grid[r][c] == 1 or (r,c) in visited:
                return 0
            # Check destination
            if r == rows - 1 and c == cols - 1:
                return 1
            #Add visited
            visited.add((r,c))
            #Check directions x 4
            count = 0
            count += dfs(grid, r+1, c, visited)
            count += dfs(grid, r, c+1, visited)
            count += dfs(grid, r-1, c, visited)
            count += dfs(grid, r, c-1, visited)
            #Remove and backtrack
            visited.remove((r,c))
            
            #Return count
            return count
        return dfs(grid, 0, 0, set())