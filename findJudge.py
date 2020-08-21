class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        candidates = set()
        for i in range(1, N + 1):
            candidates.add(i)
        trsuted = [0] * (N + 1)
        for trustSomeone, trustedPerson in trust:
            if trustSomeone in candidates:
                candidates.remove(trustSomeone)
            trsuted[trustedPerson] += 1
            
        if len(candidates) != 1:
            return -1
        judge = candidates.pop()
        if trsuted[judge] != N-1:
            return -1
        return judge
    
    #could be improved as a space wise
    #here instead of using set
        if N = 1:
            return 1
        trust_record = [0] * (N +1)
        for p1, p2 in trust:
            trust_record[p1] -= 1
            trust_record[p2] += 1
            
        for person in range(1, N+1):
            if trust_score[person] == N-1:
                return person
        return -1