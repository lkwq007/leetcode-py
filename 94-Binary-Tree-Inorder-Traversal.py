# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ret=[]
        if root is None:
            return ret
        stack=[(root,False)]
        while stack:
            node,flag=stack.pop()
            if flag:
                ret.append(node.val)
                continue
            if node.right:
                stack.append((node.right,False))
            stack.append((node,True))
            if node.left:
                stack.append((node.left,False))
        return ret
