# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        self.max_freq=1
        record={}
        def dfs(node):
            left=0
            right=0
            if node.left:
                left=dfs(node.left)
            if node.right:
                right=dfs(node.right)
            total=node.val+left+right
            if total in record:
                record[total]+=1
            else:
                record[total]=1
            self.max_freq=max(self.max_freq,record[total])
            return total
        dfs(root)
        ret=[]
        for key,val in record.items():
            if val==self.max_freq:
                ret.append(key)
        return ret