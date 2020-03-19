class Solution(object):
    def orangesRotting(self, g):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue, fresh = [], 0
        for i, r in enumerate(g):
            for j, c in enumerate(r):
                if c == 2: queue.append((i, j))
                elif c == 1: fresh += 1

        time, m, n = 0, len(g), len(g[0])                       
        while queue:
            next_q = []
            if fresh == 0: return time
            time += 1
            for i, j in queue:
                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= x < m and 0 <= y < n and g[x][y] == 1:
                        g[x][y] = 2
                        fresh -= 1                        
                        next_q.append((x, y))
            queue = next_q
        return time if fresh == 0 else -1         
            