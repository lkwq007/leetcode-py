class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        disjoint=[-1]*(len(edges)+1)
        degree=[0]*(len(edges)+1)
        def find(x):
            ret=x
            while disjoint[ret]!=-1:
                ret=disjoint[ret]
            while disjoint[x]!=-1:
                tmp=disjoint[x]
                disjoint[x]=ret
                x=tmp
            return ret
        dup=-1
        p2=-1
        for u,v in edges:
            degree[v]+=1
            if degree[v]>1:
                dup=v
                p2=u
        total=len(edges)
        for u,v in edges:
            if u==p2 and v==dup:
                continue
            if v==dup:
                p1=u
            idx1=find(u)
            idx2=find(v)
            if idx1==idx2 and dup==-1:
                return [u,v]
            if idx1!=idx2:
                disjoint[u]=idx2
                total-=1
        return [p2 if total==1 else p1,dup]

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        disjoint=[-1]*(len(edges)+1)
        degree=[0]*(len(edges)+1)
        def find(x):
            ret=x
            while disjoint[ret]>0:
                ret=disjoint[ret]
            while disjoint[x]>0 and disjoint[x]!=ret:
                tmp=disjoint[x]
                disjoint[x]=ret
                x=tmp
            return ret
        dup=-1
        p2=-1
        for u,v in edges:
            degree[v]+=1
            if degree[v]>1:
                dup=v
                p2=u
        if dup==-1:
            for u,v in edges:
                idx1=find(u)
                idx2=find(v)
                if idx1==idx2:
                    return [u,v]
                disjoint[u]=idx2
        total=len(edges)
        for u,v in edges:
            if u==p2 and v==dup:
                continue
            if v==dup:
                p1=u
            idx1=find(u)
            idx2=find(v)
            if idx1!=idx2:
                disjoint[u]=idx2
                total-=1
        if total==1:
            return [p2,dup]
        else:
            return [p1,dup]
         

# class Solution:
#     def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
#         disjoint=[-1]*(len(edges)+1)
#         degree=[0]*(len(edges)+1)
#         def find(x):
#             ret=x
#             while disjoint[ret]>0:
#                 ret=disjoint[ret]
#             while disjoint[x]>0 and disjoint[x]!=ret:
#                 tmp=disjoint[x]
#                 disjoint[x]=ret
#                 x=tmp
#             return ret
#         for v1,v2 in edges:
#             idx1=find(v1)
#             idx2=find(v2)
#             degree[v2]+=1
#             if idx1==idx2 or degree[v2]>1:
#                 return [v1,v2]
#             disjoint[idx2]=idx1