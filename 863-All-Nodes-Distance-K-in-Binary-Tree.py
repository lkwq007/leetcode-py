# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        # we can just construct a graph
        # however a direct dfs might work
        # echo node has unique value
        if root is None:
            return []
        if K<1:
            return [target.val]
        self.ret=[]
        def dfs(node,distance):
            if node is None:
                return None
            if distance==0:
                self.ret.append(node.val)
                return None
            ret=None
            if node==target:
                distance=K
                ret=K-1
            if distance:
                dfs(node.left,distance-1)
                dfs(node.right,distance-1)
            else:
                tmp=dfs(node.left,None)
                if tmp and tmp>0:
                    dfs(node.right,tmp-1)
                    ret=tmp-1
                elif tmp==0:
                    self.ret.append(node.val)
                if tmp:
                    return ret
                tmp=dfs(node.right,None)
                if tmp and tmp>0:
                    dfs(node.left,tmp-1)
                    ret=tmp-1
                elif tmp==0:
                    self.ret.append(node.val)
            return ret
        dfs(root,None)
        return self.ret