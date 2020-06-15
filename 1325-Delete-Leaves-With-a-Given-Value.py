# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        # do a post order
        if root is None:
            return root
        stack=[(root,None,False)]
        while stack:
            node,parent,flag=stack.pop()
            if flag:
                if node.val==target and node.left==None and node.right==None:
                    if parent==None:
                        root=None
                    elif parent.left==node:
                        parent.left=None
                    else:
                        parent.right=None
                continue
            stack.append((node,parent,True))
            if node.right:
                stack.append((node.right,node,False))
            if node.left:
                stack.append((node.left,node,False))
        return root