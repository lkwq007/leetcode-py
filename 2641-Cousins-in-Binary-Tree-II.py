# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # level traversal
        queue=[(root,0,None)]
        record={}
        for node,d,p in queue:
            if d not in record:
                record[d]=[]
            record[d].append((node,p))
            for next in [node.left,node.right]:
                if next:
                    queue.append((next,d+1,node))
        def process(acc,total):
            part=sum([item.val for item in acc])
            for node in acc:
                node.val=total-part
        for d,lst in record.items():
            total=sum([item[0].val for item in lst])
            last=None
            acc=[]
            for node,p in lst:
                if p==last:
                    acc.append(node)
                else:
                    process(acc,total)
                    last=p
                    acc=[node]
            process(acc,total)
        root.val=0
        return root
