# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None and root.val==sum:
            return True
        return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val) 

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        self.flag=False
        def dfs(node,acc):
            if self.flag:
                return
            if node.left==None and node.right==None:
                if acc+node.val==sum:
                    self.flag=True
            if node.left:
                dfs(node.left,acc+node.val)
            if node.right:
                dfs(node.right,acc+node.val)
        dfs(root,0)
        return self.flag