import collections
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(set)
        inDegree =collections.defaultdict(int)
        for course, preReq in prerequisites:
            graph[preReq].add(course)
            inDegree[course] += 1
            
        q = collections.deque()
        for course in graph:
            if inDegree[course] == 0:
                q.append(course)
        while q:
            course = q.pop()
            for neighbor in graph[course]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    q.append(neighbor)
        for course in inDegree:
            if inDegree[course] != 0:
                return False
        return True
        
