from typing import List
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # simply using union find is not correct
        # the testing cases might not cover all test cases
        # we have to test the in degree 
        disjoint=[-1]*n
        self.indegree=[0]*n
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
                self.indegree[left]+=1
                if union(idx,left):
                    self.total-=1
                else:
                    return False
            if right!=-1:
                self.indegree[right]+=1
                if union(idx,right):
                    self.total-=1
                else:
                    return False
            return dfs(left) and dfs(right)
        for idx in range(n):
            if disjoint[idx]==-1:
                if not dfs(idx):
                    return False
        return all(map(lambda x:x==0 or x==1,self.indegree)) and sum(self.indegree)==n-1 and self.total==1

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # the only one correct solution found in discussion
        # https://leetcode.com/problems/validate-binary-tree-nodes/discuss/517557/C%2B%2B-Find-Root-%2B-DFS
        indegree=[0]*n
        for idx in range(n):
            if leftChild[idx]!=-1:
                indegree[leftChild[idx]]+=1
            if rightChild[idx]!=-1:
                indegree[rightChild[idx]]+=1
            if indegree[leftChild[idx]]>1 or indegree[rightChild[idx]]>1:
                return False
        root=-1
        for idx in range(n):
            if indegree[idx]==0:
                if root==-1:
                    root=idx
                else:
                    return False
        def dfs(idx):
            if idx==-1:
                return 0
            return 1+dfs(leftChild[idx])+dfs(rightChild[idx])
        return dfs(root)==n

x=Solution()
print(x.validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [3,3,-1,-1]))