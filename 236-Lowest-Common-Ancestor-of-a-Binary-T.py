# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        target=[p,q]
        self.ret=None
        def dfs(node):
            ret=[False,False]
            if node==p:
                ret[0]=True
            elif node==q:
                ret[1]=True
            if node.left:
                tmp=dfs(node.left)
                ret[0]=ret[0] or tmp[0]
                ret[1]=ret[1] or tmp[1]
            if node.right:
                tmp=dfs(node.right)
                ret[0]=ret[0] or tmp[0]
                ret[1]=ret[1] or tmp[1]
            if ret[0] and ret[1] and self.ret==None:
                self.ret=node
                return [False,False]
            else:
                return ret
        dfs(root)
        return self.ret