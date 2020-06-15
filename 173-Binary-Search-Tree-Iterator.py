# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        # do inorder
        self.stack=[(root,False)] if root else []
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        while self.stack:
            node,flag=self.stack.pop()
            if flag:
                return node.val
            if node.right:
                self.stack.append((node.right,False))
            self.stack.append((node,True))
            if node.left:
                self.stack.append((node.left,False))

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.stack:
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()