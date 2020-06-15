# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # assign a no for each node
        if root is None:
            return 0
        width=[0,0]
        ret=0
        queue=[(root,0,0)]
        cur=-1
        idx=0
        while idx<len(queue):
            node,depth,no=queue[idx]
            idx+=1
            if depth!=cur:
                ret=max(ret,width[1]-width[0]+1)
                width[0]=no
                width[1]=no
                cur=depth
            else:
                width[1]=no
            if node.left:
                queue.append((node.left,depth+1,2*no))
            if node.right:
                queue.append((node.right,depth+1,2*no+1))
        ret=max(ret,width[1]-width[0]+1)
        return ret