# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            min_val=abs(root.left.val-root.val)
        else:
            min_val=abs(root.right.val-root.val)
        stack=[(root,False)]
        last=None
        while stack:
            node,flag=stack.pop()
            if flag:
                if last:
                    min_val=min(min_val,abs(node.val-last.val))
                last=node
                continue
            if node.right:
                stack.append((node.right,False))
            stack.append((node,True))
            if node.left:
                stack.append((node.left,False))
        return min_val