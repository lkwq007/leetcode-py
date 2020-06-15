# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        # Note: You may assume the tree (i.e., the given root node) is not NULL.
        queue=[(root,0)]
        idx=0
        left_most=root
        cur_depth=0
        while idx<len(queue):
            node,depth=queue[idx]
            idx+=1
            if cur_depth<depth:
                cur_depth=depth
                left_most=node
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right,depth+1))
        return left_most.val
