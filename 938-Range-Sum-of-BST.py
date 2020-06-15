# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        sum=[0]
        # this is a BST
        def dfs(node):
            if node:
                if L<=node.val<=R:
                    sum[0]+=node.val
                if node.val>L:
                    dfs(node.left)
                if node.val<R:
                    dfs(node.right)
        dfs(root)
        return sum[0]


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        sum=[0]
        def dfs(node):
            if L<=node.val<=R:
                sum[0]+=node.val
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        if root:
            dfs(root)
        return sum[0]