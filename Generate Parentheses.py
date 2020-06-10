class Solurion(object):
    def generateParenthesis(self, n):
        res = []
        self.dfs(n, n, "", res)
        return res
    def dfs(self, op, cl, path, res):
        # prunning cases:
        if cl < op or op < 0 or cl <0:
            return
        if op == 0 and cl ==0:
            res.append(path)
        else:
            dfs(op -1, cl, path + "(", res)
            dfs(op, cl -1, path + ")", res)

