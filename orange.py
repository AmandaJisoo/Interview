class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rowMax, colMax = len(grid), len(grid[0])
        freshCount = 0
        q = collections.deque()
        for i in range(rowMax):
            for j in range(colMax):
                if grid[i][j] ==  1:
                    freshCount += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        res = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for x,y in [(i + 1, j), (i -1, j), (i, j + 1), (i, j-1)]:
                    if 0 <= x < rowMax and 0 <= y < colMax and grid[x][y] == 1:
                        grid[x][y] = 2
                        freshCount -= 1
                        q.append((x,y))
            res += 1
        return max(0, res -1) if freshCount == 0 else -1
