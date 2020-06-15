# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        h=-1
        node=root
        while node:
            h+=1
            node=node.left
        self.cnt=0
        def dfs(node,depth):
            if depth==h:
                self.cnt+=1
                return
            if node.left is None and depth==h-1:
                return
            if node.left:
                dfs(node.left,depth+1)
            if node.right is None and depth==h-1:
                return
            if node.right:
                dfs(node.right,depth+1)
        dfs(root,0)
        return 2**(h+1)-1-2**h+self.cnt

x=Solution()
print(x.countNodes(TreeNode(1)))