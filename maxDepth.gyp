class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1
        return max(left, right)