# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        self.ret=[]
        queue=[(root,0)]
        cur=-1
        idx=0
        max_val=root.val
        while idx<len(queue):
            node,depth=queue[idx]
            idx+=1
            if cur!=depth:
                self.ret.append(max_val)
                max_val=node.val
                cur+=1
            else:
                max_val=max(max_val,node.val)
            if node.left:
                queue.append((node.left,depth+1))
            if node.right:
                queue.append((node.right,depth+1))
        self.ret.append(max_val)
        return self.ret[1:]