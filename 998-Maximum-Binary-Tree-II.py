# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        def dfs(node):
            if node is None or node.val<=val:
                tmp=TreeNode(val)
                tmp.left=node
                return tmp
            node.right=dfs(node.right)
            return node
        return dfs(root)