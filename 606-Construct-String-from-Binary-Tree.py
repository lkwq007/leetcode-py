# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if t is None:
            return ""
        self.ret=""
        def dfs(node:TreeNode):
            self.ret+=str(node.val)
            if node.left is None and node.right is None:
                return
            if node.left:
                self.ret+="("
                dfs(node.left)
                self.ret+=")"
            else:
                self.ret+="()"
            if node.right:
                self.ret+="("
                dfs(node.right)
                self.ret+=")"
            return
        dfs(t)
        return self.ret