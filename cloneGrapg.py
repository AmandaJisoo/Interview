import collections
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        '''
        idea: mapping the original node to a new node -> fast guranteed acess
        do BFS from the start node
        if the neighbor has not been seen yet, create a node add it to its neighbor and add it to q
        if it is not in the dictionary, it means it has been seen which means 
        so just only add to the curent node's neighbor
        '''
        if not node:
            return
        copiedNode = Node(node.val, [])
        dic = {node: copiedNode}
        q = collections.deque([node])
        while q:
            node = q.popleft()
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    neighborCopy = Node(neighbor.val, [])
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    q.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return copiedNode