# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        stack=[(root,False)]
        last=None
        while stack:
            node,flag=stack.pop()
            if flag:
                if last is None:
                    last=node.val
                elif last>=node.val:
                    return False
                last=node.val
                continue
            if node.right:
                stack.append((node.right,False))
            stack.append((node,True))
            if node.left:
                stack.append((node.left,False))
        return True