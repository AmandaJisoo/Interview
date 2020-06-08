# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, node, target):
        if not node:
            return False
        elif not node.left and not node.right:
            return node.val == target
        else:
            return self.hasPathSum(node.left, target-node.val) or self.hasPathSum(node.right, target-node.val)