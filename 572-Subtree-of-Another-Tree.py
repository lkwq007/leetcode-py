# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if t is None or s is None:
            return True
        def validate(n1,n2):
            if n1 is None and n2 is None:
                return True
            if n1 is None or n2 is None:
                return False
            if n1.val==n2.val:
                return validate(n1.left,n2.left) and validate(n1.right,n2.right)
            return False 
        def dfs(node):
            ret=False
            if node.val==t.val:
                ret=validate(node,t)
            if ret:
                return ret
            if node.left:
                ret=dfs(node.left)
            if ret: return ret
            if node.right:
                return dfs(node.right)
        return dfs(s)