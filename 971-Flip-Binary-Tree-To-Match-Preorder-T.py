# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        if root is None or len(voyage)<1:
            return []
        if root.val!=voyage[0]:
            return [-1]
        self.ret=[]
        self.idx=1
        def dfs(node):
            if node.left and node.right:
                if node.left.val==voyage[self.idx]:
                    self.idx+=1
                    dfs(node.left)
                    dfs(node.right)
                elif node.right.val==voyage[self.idx]:
                    self.idx+=1
                    self.ret.append(node.val)
                    dfs(node.right)
                    dfs(node.left)
                else:
                    self.ret=[-1]
            elif node.left:
                if node.left.val==voyage[self.idx]:
                    self.idx+=1
                    dfs(node.left)
                else:
                    self.ret=[-1]
            elif node.right:
                if node.right.val==voyage[self.idx]:
                    self.idx+=1
                    dfs(node.right)
                else:
                    self.ret=[-1]
        dfs(root)
        if self.idx