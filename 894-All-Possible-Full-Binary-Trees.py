# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import functools
class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        def copy(node):
            if node is None:
                return None
            root=TreeNode()
            root.left=copy(node.left)
            root.right=copy(node.right)
            return root
        @functools.lru_cache(maxsize=None)
        def probe(n):
            if n==1:
                return [TreeNode()]
            ret=[]
            # n-2+1
            for i in range(1,n-2+1,2):
                left=probe(i)
                right=probe(n-1-i)
                for l in left:
                    for r in right:
                        node=TreeNode()
                        node.left=l
                        node.right=r
                        ret.append(node)
            return ret
        return probe(N)