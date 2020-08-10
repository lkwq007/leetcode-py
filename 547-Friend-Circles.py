# A DFS will also work fine
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        total=len(M)
        disjoint=[-1]*total
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
            a_idx=search(a)
            b_idx=search(b)
            if a_idx!=b_idx:
                disjoint[b_idx]=a_idx
        for i in range(total):
            for j in range(i+1,total):
                if M[i][j]:
                    union(i,j)
        ret=0
        for i in range(total):
            if disjoint[i]<0:
                ret+=1
        return ret

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        total=len(M)
        disjoint=[-1]*total
        self.cnt=total
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
            a_idx=search(a)
            b_idx=search(b)
            if a_idx!=b_idx:
                disjoint[b_idx]=a_idx
                self.cnt-=1
        for i in range(total):
            for j in range(i+1,total):
                if M[i][j]:
                    union(i,j)
        return self.cnt

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        total=len(M)
        visited=[False]*total
        def dfs(idx):
            visited[idx]=True
            for i in range(total):
                if M[idx][i] and not visited[i]:
                    dfs(i)
        ret=0
        for i in range(total):
            if not visited[i]:
                dfs(i)
                ret+=1
        return ret