# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []
        self.ret=[]
        def dfs(node,path):
            tmp=path+"->"+str(node.val)
            if node.left==None and node.right==None:
                self.ret.append(tmp[2:])
                return
            if node.left:
                dfs(node.left,tmp)
            if node.right:
                dfs(node.right,tmp)
        dfs(root,"")
        return self.ret