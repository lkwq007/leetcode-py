# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root is None:
            return 0
        cnt=1 if root.val==sum else 0
        self.cnt=0
        self.record={0:1}
        def dfs(node,acc):
            if node is None:
                return
            acc+=node.val
            rest=acc-sum
            if rest in self.record:
                self.cnt+=self.record[rest]
            if acc in self.record:
                self.record[acc]+=1
            else:
                self.record[acc]=1
            dfs(node.left,acc)
            dfs(node.right,acc)
            self.record[acc]-=1
        dfs(root,0)
        return self.cnt

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root is None:
            return 0
        cnt=1 if root.val==sum else 0
        self.cnt=0
        def dfs(node,stack):
            if node is None:
                return
            stack.append(0)
            for idx in range(0,len(stack)):
                stack[idx]+=node.val
                if stack[idx]==sum:
                    self.cnt+=1
            dfs(node.left,stack)
            dfs(node.right,stack)
            for idx in range(0,len(stack)):
                stack[idx]-=node.val
            stack.pop()
        dfs(root,[])
        return self.cnt