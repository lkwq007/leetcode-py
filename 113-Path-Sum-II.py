# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root is None:
            return []
        self.ret=[]
        def dfs(node,path,acc):
            tmp=node.val+acc
            path.append(node.val)
            if node.left==None and node.right==None:
                if tmp==sum:
                    self.ret.append(path[:])
                path.pop()
                return
            if node.left:
                dfs(node.left,path,tmp)
            if node.right:
                dfs(node.right,path,tmp)
            path.pop()
        dfs(root,[],0)
        return self.ret            