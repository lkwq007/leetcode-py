# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder)<1 or len(inorder)<1:
            return None
        self.root_idx=0
        def construct(lst):
            if not lst:
                return None
            root=preorder[self.root_idx]
            self.root_idx+=1
            for idx in range(0,len(lst)):
                if lst[idx]==root:
                    break
            node=TreeNode(root)
            node.left=construct(lst[:idx])
            node.right=construct(lst[(idx+1):])
            return node
        return construct(inorder)
