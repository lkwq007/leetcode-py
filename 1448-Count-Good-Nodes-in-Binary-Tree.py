# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.cnt=0
        def dfs(node,val):
            if node.val>=val:
                self.cnt+=1
            tmp=max(node.val,val)
            if node.left:
                dfs(node.left,tmp)
            if node.right:
                dfs(node.right,tmp)
        dfs(root,root.val)
        return self.cnt