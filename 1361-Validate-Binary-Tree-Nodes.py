from typing import List
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        disjoint=[-1]*n
        self.total=n
        def search(idx):
            tmp=idx
            while disjoint[tmp]!=-1:
                tmp=disjoint[tmp]
            ret=tmp
            while disjoint[idx]!=-1:
                tmp=disjoint[idx]
                disjoint[idx]=ret
                idx=tmp
            return ret
        def union(a,b):
            a_set=search(a)
            b_set=search(b)
            if a_set==b_set:
                return False
            disjoint[b_set]=a_set
            return True
        def dfs(idx):
            if idx==-1:
                return True
            left=leftChild[idx]
            right=rightChild[idx]
            if left!=-1:
                if union(idx,left):
                    self.total-=1
                else:
                    return False
            if right!=-1:
                if union(idx,right):
                    self.total-=1
                else:
                    return False
            return dfs(left) and dfs(right)
        for idx in range(n):
            if disjoint[idx]==-1:
                if not dfs(idx):
                    return False
        return self.total==1
    
x=Solution()
print(x.validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [-1,3,-1,-1]))