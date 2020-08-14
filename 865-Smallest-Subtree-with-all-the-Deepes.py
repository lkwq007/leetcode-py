# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        self.max=0
        self.cnt=0
        def depth(node,acc):
            if acc==self.max:
                self.cnt+=1
            elif acc>self.max:
                self.max=acc
                self.cnt=1
            if node.left:
                depth(node.left,acc+1)
            if node.right:
                depth(node.right,acc+1)
        depth(root,0)
        self.ret=
        def dfs(node,acc):
            left=dfs(node.left,acc+1) if node.left else 0
            right=dfs(node.right,acc+1) if node.right else 0
            if left+right==self.cnt:
