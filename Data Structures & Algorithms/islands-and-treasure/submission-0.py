from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        bfs_queue = deque()
        val = 1
        for row in range(len(grid)):
            for col in range(len(grid[row])): 
                if grid[row][col] == 0:
                    bfs_queue.append((row+1, col, val))
                    bfs_queue.append((row-1, col, val))
                    bfs_queue.append((row, col+1, val))
                    bfs_queue.append((row, col-1, val))
        while len(bfs_queue) > 0:
            curr_row, curr_col, val = bfs_queue.popleft()
            if curr_row >= len(grid) or curr_row < 0 or curr_col < 0 or curr_col >= len(grid[row]):
                continue
            curr = grid[curr_row][curr_col]
            if curr == 2147483647:
                grid[curr_row][curr_col] = val
                bfs_queue.append((curr_row+1, curr_col, val+1))
                bfs_queue.append((curr_row-1, curr_col, val+1))
                bfs_queue.append((curr_row, curr_col+1, val+1))
                bfs_queue.append((curr_row, curr_col-1, val+1))