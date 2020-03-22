class Solution(object):

    def numlands(self, grid):
        # BFS
        if not grid:
            return 0
        maxRow, maxCol, count = len(grid), len(grid[0]), 0
        for i in range(maxRow):
            for j in range(maxCol):
                if grid[i][j] == "1":
                    count += 1
                    stack = [(i,j)]
                    for ii,jj in stack:
                        if 0<=ii<maxRow and 0<=jj<maxCol and grid[ii][jj] == "1":
                            grid[ii][jj] = "2"
                            stack.extend([(ii+1,jj),(ii-1,jj),(ii,jj-1),(ii,jj+1)])
        return count