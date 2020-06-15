# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.total=0
        def dfs(node,acc):
            tmp=10*acc+node.val
            if node.left==None and node.right==None:
                self.total+=tmp
                return
            if node.left:
                dfs(node.left,tmp)
            if node.right:
                dfs(node.right,tmp)
        dfs(root,0)
        return self.total