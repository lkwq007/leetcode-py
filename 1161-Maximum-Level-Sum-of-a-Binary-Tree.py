# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if root is None:
            return 1
        queue=[(root,1)]
        idx=0
        acc=0
        ret=1
        last=1
        max_val=root.val
        while idx<len(queue):
            node,level=queue[idx]
            idx+=1
            if level!=last:
                if acc>max_val:
                    max_val=acc
                    ret=last
                last=level
                acc=node.val
            else:
                acc+=node.val
            if node.left:
                queue.append((node.left,level+1))
            if node.right:
                queue.append((node.right,level+1))
        if acc>max_val:
            ret=level
        return ret

        
