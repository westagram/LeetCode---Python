class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Create a visited tracking matrix
        # Loop through row and col using dfs, if not visited and value is 1, dfs the 1s around it
        nRow, nCol = len(grid), len(grid[0])
        visited = [[False] * nCol for _ in range(nRow)]
        total = 0
        for row in range(nRow):
            for col in range(nCol):
                if not visited[row][col] and grid[row][col] == "1":
                    self.dfs(row, col, grid, visited)
                    total += 1
        return total

    def dfs(self, row, col, grid, visited):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return
        if grid[row][col] == "0" or visited[row][col]:
            return
        visited[row][col] = True
        self.dfs(row+1, col, grid, visited)
        self.dfs(row-1, col, grid, visited)
        self.dfs(row, col+1, grid, visited)
        self.dfs(row, col-1, grid, visited)