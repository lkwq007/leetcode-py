# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.sum=0
        def dfs_depth(node,depth=2):
            if depth==0:
                self.sum+=node.val
            else:
                if node.left:
                    dfs_depth(node.left,depth-1)
                if node.right:
                    dfs_depth(node.right,depth-1)
        def dfs(node):
            if node.val%2==0:
                dfs_depth(node)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)
        return self.sum