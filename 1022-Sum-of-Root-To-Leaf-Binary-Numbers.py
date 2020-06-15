# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.total=0
        def dfs(node,acc):
            val=(acc<<1)+node.val
            if node.left is None and node.right is None:
                self.total+=val
            if node.left:
                dfs(node.left,val)
            if node.right:
                dfs(node.right,val)
        dfs(root,0)
        return self.total