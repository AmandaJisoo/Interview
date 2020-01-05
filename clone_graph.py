"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
from collections import deque
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Nodec
        """        
        q = deque()
        gMap = {}
        q.append(node)
        visited = {node.val}
        while q:
            #original node from a graph
            n = q.popleft()
            
            #if the new node has not been created then create a deep copy
            if n.val not in gMap:
                gMap[n.val] = Node(n.val, [])
                
            #grab a deep copy node
            new_node = gMap[n.val]
            
            #iterate throgh neighbor
            # and create a deep copy along the way
            for neighbor in n.neighbors:
                if neighbor.val not in visited:
                    q.append(neighbor)
                    visited.add(neighbor.val)
                    if neighbor.val not in gMap:
                        gMap[neighbor.val] = Node(neighbor.val, [])
                new_node.neighbors.append(gMap[neighbor.val])

        return gMap[node.val]