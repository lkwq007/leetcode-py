# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        if root is None:
            return []
        self.record={}
        # hash tree?
        def dfs(node):
            left="n"
            right="n"
            if node.left:
                left=dfs(node.left)
            if node.right:
                right=dfs(node.right)
            sig=left+"-"+str(node.val)+"-"+right
            if sig in self.record:
                self.record[sig]=node
            else:
                self.record[sig]=None
            return sig
        dfs(root)
        ret=[]
        for key,val in self.record.items():
            if val:
                ret.append(val)
        return ret
                

