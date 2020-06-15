# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d<1:
            return root
        if d==1:
            node=TreeNode(v)
            node.left=root
            return node
        def dfs(node,depth):
            if depth==d:
                tmp=TreeNode(v)
                tmp.left=node.left
                node.left=tmp
                tmp=TreeNode(v)
                tmp.right=node.right
                node.right=tmp
                return
            if node.left:
                dfs(node.left,depth+1)
            if node.right:
                dfs(node.right,depth+1)
        dfs(root,2)
        return root