"""
# Definition for a Node.

"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        graph=[None]*101
        def clone(node):
            if node is None:
                return None
            if graph[node.val] is None:
                tmp=Node(node.val)
                graph[node.val]=tmp
                for item in node.neighbors:
                    item_clone=clone(item)
                    tmp.neighbors.append(item_clone)
            return graph[node.val]
        return clone(node)