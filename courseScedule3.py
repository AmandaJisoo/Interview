import heapq

class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        # sort by earlest duedate
        courses.sort(key=lambda k: k[1])

        que = []
        cur = 0

        # use min(-max will be poped) heap to remove biggest duration
        for duration, due in courses:
            heapq.heappush(que, -duration)
            cur += duration
            if cur > due:
                removed = heapq.heappop(que)
                cur += removed

        return len(que)
