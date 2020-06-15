# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        seq1=[]
        seq2=[]
        def dfs(node,seq):
            if node.left is None and node.right is None:
                seq.append(node.val)
            if node.left:
                dfs(node.left,seq)
            if node.right:
                dfs(node.right,seq)
        dfs(root1,seq1)
        dfs(root2,seq2)
        return seq1==seq2