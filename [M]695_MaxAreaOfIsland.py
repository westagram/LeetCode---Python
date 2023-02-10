class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Creating a tracking matrix
        # Loop through matrix and keep track of visited
        # Calculate the surrounding island using dfs

        tracking = [[False]*len(grid[0]) for _ in range(len(grid))]

        maxSum = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if tracking[row][col]:
                    continue
                if grid[row][col]:
                    print("BREAK", row, col)
                    total = self.dfs(row, col, tracking, grid, 0)
                    maxSum = max(total, maxSum)

        return maxSum


    def dfs(self, row, col, tracking, grid, total):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or not grid[row][col]:
            return total
        if tracking[row][col]:
            return total
        total += 1
        tracking[row][col] = True
        total = self.dfs(row+1, col, tracking, grid, total)
        total = self.dfs(row-1, col, tracking, grid, total)
        total = self.dfs(row, col+1, tracking, grid, total)
        total = self.dfs(row, col-1, tracking, grid, total)
        return total