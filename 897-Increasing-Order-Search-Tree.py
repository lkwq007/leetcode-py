# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        stack=[(root,False)]
        dummy=TreeNode(0)
        last=dummy
        while stack:
            node,flag=stack.pop()
            if flag:
                last.right=node
                node.left=None
                last=node
                continue
            if node.right:
                stack.append((node.right,False))
            stack.append((node,True))
            if node.left:
                stack.append((node.left,False))
        root=dummy.right
        return root
