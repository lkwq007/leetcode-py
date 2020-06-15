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
        for v1,v2 in edges:
            idx1=find(v1)
            idx2=find(v2)
            degree[v2]+=1
            if idx1==idx2 or degree[v2]>1:
                return [v1,v2]
            disjoint[idx2]=idx1