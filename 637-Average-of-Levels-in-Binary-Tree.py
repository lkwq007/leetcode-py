# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        # non-empty
        queue=[(root,0)]
        ret=[]
        acc=0.0
        cur=-1
        idx=0
        cnt=1
        while idx<len(queue):
            node,depth=queue[idx]
            idx+=1
            if depth!=cur:
                cur=depth
                ret.append(acc/cnt)
                cnt=1
                acc=0.0+node.val
            else:
                cnt+=1
                acc+=node.val
            if node.left:
                queue.append((node.left,depth+1))
            if node.right:
                queue.append((node.right,depth+1))
        ret.append(acc/cnt)
        return ret[1:]