"""
# Definition for a Node.

"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        def dfs(node,depth):
            depth+=1
            max=0
            if node.children:
                for item in node.children:
                    tmp=dfs(item,depth)
                    if tmp>max:
                        max=tmp
                return max
            return depth
        return dfs(root,0)