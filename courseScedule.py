import collections
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        inDegree = collections.defaultdict(int)
        graph = collections.defaultdict(set)
        
        for cur, pre in prerequisites:
            graph[pre].add(cur)
            inDegree[cur] += 1
            
        bfs = [i for i in range(numCourses) if inDegree[i] == 0]
        
        for i in bfs:
            for j in graph[i]:
                inDegree[j] -= 1
                if (inDegree[j] == 0):
                    bfs.append(j)
                    
        return bfs if len(bfs) == numCourses else []