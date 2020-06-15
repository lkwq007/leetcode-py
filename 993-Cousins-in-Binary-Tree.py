# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root is None:
            return False
        # we know the range of val
        mapping=[(-1,None),(-1,None)]
        def dfs(node,parent,depth):
            if node.val==x:
                mapping[0]=(depth,parent)
            if node.val==y:
                mapping[1]=(depth,parent)
            if node.left:
                dfs(node.left,node,depth+1)
            if node.right:
                dfs(node.right,node,depth+1)
        dfs(root,None,0)
        return mapping[0][0]>0 and mapping[0][0]==mapping[1][0] and mapping[0][1]!=mapping[1][1]


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root is None:
            return False
        # we know the range of val
        mapping=[-1]*101
        mapping[0]=True
        def dfs(node,depth):
            mapping[node.val]=depth
            if node.left and node.right:
                if node.left.val==x and node.right.val==y:
                    mapping[0]=False
                    return
                if node.left.val==y and node.right.val==x:
                    mapping[0]=False
                    return
            if node.left:
                dfs(node.left,depth+1)
            if node.right:
                dfs(node.right,depth+1)
        dfs(root,0)
        return mapping[x]==mapping[y] and mapping[x]>0 and mapping[0]