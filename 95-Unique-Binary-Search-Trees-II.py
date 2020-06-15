# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n==0:
            return []
        def construct(left,right):
            if left==right:
                return [None]
            ret=[]
            for idx in range(left,right):
                ret_left=construct(left,idx)
                ret_right=construct(idx+1,right)
                for i in range(0,len(ret_left)):
                    for j in range(0,len(ret_right)):
                        node=TreeNode(idx,ret_left[i],ret_right[j])
                        ret.append(node)
            return ret
        return construct(1,n+1)
