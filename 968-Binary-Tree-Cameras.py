# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        if root is None:
            return 0
        def dfs(node):
            if node.left is None and node.right is None:
                return 1,1,0
            left=[1,0,0]
            right=[1,0,0]
            # three cases
            # - node has a camera
            # - node is covered, no camera
            # - node is not covered
            if node.left:
                left=dfs(node.left)
            if node.right:
                right=dfs(node.right)
            camera_here=left[0]+right[0]
            for l in left:
                for r in right:
                    camera_here=min(camera_here,l+r)
            # a camera is installed in this node
            camera_here+=1
            # node is covered, no camera installed
            covered=min(left[0]+right[0],left[0]+right[1],left[1]+right[0])
            # node is not covered
            not_covered=left[1]+right[1]
            return camera_here,covered,not_covered
        a,b,_=dfs(root)
        return min(a,b)