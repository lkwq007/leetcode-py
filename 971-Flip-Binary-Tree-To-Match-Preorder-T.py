# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        if root is None or len(voyage)<1 or root.val!=voyage[0]:
            return [-1]
        self.ret=[]
        self.idx=0
        def dfs(node):
            if node.val==voyage[self.idx]:
                self.idx+=1
            else:
                self.ret=[-1]
                return
            if node.left and node.right:
                if node.right.val==voyage[self.idx]:
                    self.ret.append(node.val)
                    dfs(node.right)
                    dfs(node.left)
                elif node.left.val==voyage[self.idx]:
                    dfs(node.left)
                    dfs(node.right)
                else:
                    self.ret=[-1]
            elif node.left:
                if node.left.val==voyage[self.idx]:
                    dfs(node.left)
                else:
                    self.ret=[-1]
            elif node.right:
                if node.right.val==voyage[self.idx]:
                    dfs(node.right)
                else:
                    self.ret=[-1]
        dfs(root)
        return self.ret if len(self.ret)==0 or self.ret[0]!=-1 else [-1]