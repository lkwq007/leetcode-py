# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder)<1 or len(postorder)<1:
            return None
        self.root=len(postorder)-1
        def construct(lst):
            if not lst:
                return None
            root=postorder[self.root]
            for idx in range(0,len(lst)):
                if root==lst[idx]:
                    break
            self.root-=1
            node=TreeNode(root)
            node.right=construct(lst[(idx+1):])
            node.left=construct(lst[:idx])
            return node
        return construct(inorder)