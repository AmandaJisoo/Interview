# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        elif not root.left:
            return self.minDepth(root.right)+1
        elif not root.right:
            return self.minDepth(root.left)+1
        else:
            #both not null: general case
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)
            return min(left, right) + 1
        