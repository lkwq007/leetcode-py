# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        self.flag=False
        def dfs(node):
            if node is None:
                return 0
            if self.flag:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            if node.val==x:
                top=n-left-right-1
                tmp=n//2
                if top>tmp or left>tmp or right>tmp:
                    self.flag=True
            return left+right+1
        dfs(root)
        return self.flag
