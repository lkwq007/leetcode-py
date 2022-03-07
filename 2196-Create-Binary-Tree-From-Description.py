# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # topo sort
        queue=[]
        degree={}
        record={}
        mapping={}
        for par,child,left in descriptions:
            degree[child]=degree.get(child,0)
            degree[par]=degree.get(par,0)+1
            record[child]=(par,left)
        for k,v in degree.items():
            if v==0:
                queue.append(k)
        while queue:
            target=[]
            for item in queue:
                if item not in record:
                    return mapping[item]
                par,left=record[item]
                if par not in mapping:
                    mapping[par]=TreeNode(val=par)
                if item not in mapping:
                    mapping[item]=TreeNode(val=item)
                node=mapping[par]
                child=mapping[item]
                if left:
                    node.left=child
                else:
                    node.right=child
                degree[par]-=1
                if degree[par]==0:
                    target.append(par)
            queue=target
        return None
                

