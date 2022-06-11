class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        lst=[-1]*n
        def find(x):
            ret=x
            while lst[ret]>-1:
                ret=lst[ret]
            while lst[x]>-1:
                tmp=lst[x]
                lst[x]=ret
                x=tmp
            return ret
        def union(a,b):
            ai=find(a)
            bi=find(b)
            if ai==bi:
                return
            if lst[ai]>lst[bi]:
                ai,bi=bi,ai
            lst[ai]+=lst[bi]
            lst[bi]=ai
        edgeList.sort(key=lambda x:x[-1])
        idx_lst=list(range(len(queries)))
        idx_lst.sort(key=lambda x:queries[x][-1])
        pos=0
        ret=[False]*len(queries)
        for idx in idx_lst:
            p,q,limit=queries[idx]
            while pos<len(edgeList) and edgeList[pos][-1]<limit:
                u,v,d=edgeList[pos]
                union(u,v)
                pos+=1
            pi=find(p)
            qi=find(q)
            if pi==qi:
                ret[idx]=True
        return ret