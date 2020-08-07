# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        # treat root as 0,0
        record={}
        def dfs(node,x,y):
            if node:
                if x in record:
                    record[x].append((-y,node.val))
                else:
                    record[x]=[(-y,node.val)]
                dfs(node.left,x-1,y-1)
                dfs(node.right,x+1,y-1)
        dfs(root,0,0)
        ret=[]
        keys=list(record.keys())
        keys.sort()
        for key in keys:
            lst=sorted(record[key])
            ret.append(list(map(lambda x:x[1],lst)))
        return ret