class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    self.explore(grid,i, j)
                    counter+=1
        return counter

    def explore(self, grid: List[List[str]], x = int, y = int):
        grid[x][y] = "0"
        if x + 1 < (len(grid)) and grid[x+1][y] == "1":
            self.explore(grid, x+1, y)
        if y + 1 < (len(grid[x])) and grid[x][y+1] == "1":
            self.explore(grid, x, y+1)
        if y - 1 > -1 and grid[x][y-1] == "1":
            self.explore(grid, x, y-1)
        if x - 1 > -1 and grid[x-1][y] == "1":
            self.explore(grid, x-1, y)
        return None
        

        