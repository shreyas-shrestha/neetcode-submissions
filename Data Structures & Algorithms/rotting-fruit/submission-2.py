class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        num_fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                elif grid[i][j] == 1:
                    num_fresh+=1
        longest_time = 0
        while len(queue) > 0:
            i, j, time = queue.pop(0)
            if i - 1 >= 0 and grid[i-1][j] == 1:
                num_fresh-=1
                grid[i-1][j] = 2
                queue.append((i-1, j, time+1))
                if time + 1 > longest_time:
                    longest_time = time + 1
            if i + 1 < len(grid) and grid[i+1][j] == 1:
                num_fresh-=1
                grid[i+1][j] = 2
                queue.append((i+1, j, time+1))
                if time + 1 > longest_time:
                    longest_time = time + 1
            if j - 1 >= 0 and grid[i][j-1] == 1:
                num_fresh-=1
                grid[i][j-1] = 2
                queue.append((i, j-1, time+1))
                if time + 1 > longest_time:
                    longest_time = time + 1
            if j + 1 < len(grid[i]) and grid[i][j+1] == 1:
                num_fresh-=1
                grid[i][j+1] = 2
                queue.append((i, j+1, time+1))
                if time + 1 > longest_time:
                    longest_time = time + 1
        if num_fresh > 0:
            return -1
        return longest_time


        