class Solution(object):
    # recursive
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.res = None
        self.inOrder(root)
        return self.res
    
    def inOrder(self, node):
        if not node:
            return 
        self.inOrder(node.left)
        self.k -= 1
        if self.k == 0:
            self.res = node.val
            return 
        self.inOrder(node.right)

class Solution(object):
    def kthSmallest(self, root, k):
        s = []
        while root or s:
            while root:
                s.append(root)
                root = root.left
            s.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
            
    
        