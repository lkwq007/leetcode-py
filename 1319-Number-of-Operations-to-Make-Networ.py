class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        # connected components
        disjoint=[-1]*n
        def find(x):
            idx=x
            while disjoint[idx]!=-1:
                idx=disjoint[idx]
            while disjoint[x]!=-1:
                tmp=disjoint[x]
                disjoint[x]=idx
                x=tmp
            return idx
        self.total=n
        def union(a,b):
            a_idx=find(a)
            b_idx=find(b)
            if a_idx!=b_idx:
                disjoint[b_idx]=a_idx
                self.total-=1
        for u,v in connections:
            union(u,v)
        return self.total-1