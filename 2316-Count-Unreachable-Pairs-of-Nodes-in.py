class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        disjoint=[-1]*n
        def find(x):
            ret=x
            while disjoint[ret]>-1:
                ret=disjoint[ret]
            while disjoint[x]>-1:
                tmp=disjoint[x]
                disjoint[x]=ret
                x=tmp
            return ret
        def union(a,b):
            ai=find(a)
            bi=find(b)
            if ai==bi:
                return
            if disjoint[ai]>disjoint[bi]:
                ai,bi=bi,ai
            disjoint[ai]+=disjoint[bi]
            disjoint[bi]=ai
        for u,v in edges:
            union(u,v)
        acc=0
        for item in disjoint:
            if item<0:
                acc+=(-item)*(n+item)
        return acc//2