# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(x):
            if x.left is None and x.right is None:
                return (1,x.val,1)
            ret=0
            acc=x.val
            cnt=1
            if x.left:
                val=dfs(x.left)
                ret+=val[0]
                acc+=val[1]
                cnt+=val[2]
            if x.right:
                val=dfs(x.right)
                ret+=val[0]
                acc+=val[1]
                cnt+=val[2]
            if x.val==acc//cnt:
                ret+=1
            return ret,acc,cnt
        return dfs(root)[0]