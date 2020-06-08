class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        self.helper(res, root, 0)
        return res
            
    def helper(self, res, root, level):
        if not root:
            return
        if len(res) <= level:
            curLv = []
            curLv.append(root.val)
            res.append(curLv)
        else:
            #get the exising list
            exisitingLi = res[level]
            exisitingLi.append(root.val)
        self.helper(res, root.left, level + 1)
        self.helper(res, root.right, level + 1)
            