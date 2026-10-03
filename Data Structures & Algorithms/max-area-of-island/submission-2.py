class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        highestValue = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    value = self.explore(grid, row, col, 1)
                    if value > highestValue:
                        highestValue = value
        return highestValue

    def explore(self, grid: List[List[int]], row: int, col: int, value: int) -> int:
        grid[row][col] = 0
        if row + 1 < len(grid) and grid[row+1][col] == 1:
            value = self.explore(grid, row+1, col, value + 1)
        if col + 1 < len(grid[row]) and grid[row][col+1] == 1:
            value = self.explore(grid, row, col+1, value + 1)
        if col - 1 >= 0 and grid[row][col-1] == 1:
            value = self.explore(grid, row, col-1, value + 1)
        if row - 1 >= 0 and grid[row-1][col] == 1:
            value = self.explore(grid, row-1, col, value + 1)
        return value
        