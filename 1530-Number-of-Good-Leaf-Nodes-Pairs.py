# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        if root is None:
            return 0
        self.ret=0
        def dfs(node):
            if node.left is None and node.right is None:
                return [1]
            left=dfs(node.left) if node.left else []
            right=dfs(node.right) if node.right else []
            for l in left:
                for r in right:
                    if l+r<=distance:
                        self.ret+=1
            ret=[]
            for item in left+right:
                tmp=item+1
                if tmp<distance:
                    ret.append(tmp)
            return ret
        dfs(root)
        return self.ret