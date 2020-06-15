# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        # do level traversal
        if root is None:
            return True
        queue=[(root,0)]
        cur=-1
        idx=0
        cnt=0
        flag=False
        while idx<len(queue):
            node,depth=queue[idx]
            idx+=1
            if cur!=depth:
                cur=depth
                if flag:
                    cnt+=1
                flag=False
            if flag and node:
                return False
            if node is None:
                flag=True
            else:
                queue.append((node.left,depth+1))
                queue.append((node.right,depth+1))
        if flag:
            cnt+=1
        return cnt<2
