# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        self.height=0
        def dfs(node,cnt):
            if node.left is None and node.right is None:
                self.height=max(cnt,self.height)
            if node.left:
                dfs(node.left,cnt+1)
            if node.right:
                dfs(node.right,cnt+1)
        dfs(root,1)
        width=2**self.height-1
        template=[""]*width
        ret=[template[:] for i in range(0,self.height)]
        center=width//2
        def fill(node,height,pos,width):
            val=node.val
            half_width=(width-1)//2
            offset=half_width//2+1
            ret[height][pos]=str(val)
            if node.left:
                fill(node.left,height+1,pos-offset,half_width)
            if node.right:
                fill(node.right,height+1,pos+offset,half_width)
        fill(root,0,center,width)
        return ret