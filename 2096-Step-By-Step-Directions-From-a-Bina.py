# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # LCA
        self.ret=""
        def dfs(node,d):
            if node is None:
                return False,False,""
            ret=""
            lflag0,lflag1,left=dfs(node.left,"L")
            rflag0,rflag1,right=dfs(node.right,"R")
            if node.val==startValue:
                lflag0=True
                rflag0=True
            elif node.val==destValue:
                lflag1=True
                rflag1=True
            if lflag0 and rflag1:
                self.ret=left+right
                return False,False,""
            elif lflag1 and rflag0:
                self.ret=right+left
                return False,False,""
            if lflag0 or rflag0:
                ret=left+right+"U"
            if rflag1:
                ret=d+right
            if lflag1:
                ret=d+left
            return lflag0 or rflag0, lflag1 or rflag1, ret
        dfs(root,"")
        return self.ret
            
            