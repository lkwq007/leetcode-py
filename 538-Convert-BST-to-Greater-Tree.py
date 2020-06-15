# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        def search(node,acc):
            rret=0
            lret=0
            if node.right:
                rret=search(node.right,acc)
            if node.left:
                lret=search(node.left,acc+rret+node.val)
            node.val+=rret+acc
            return lret+node.val-acc
        search(root,0)
        return root