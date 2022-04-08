class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        ret=[False]*len(requests)
        disjoint=[-1]*n
        graph=[{} for _ in range(n)]
        for a,b in restrictions:
            graph[a][b]=1
            graph[b][a]=1
        def find(x):
            ret=x
            while disjoint[ret]>-1:
                ret=disjoint[ret]
            while disjoint[x]>-1:
                tmp=disjoint[x]
                disjoint[x]=ret
                x=tmp
            return ret
        for i in range(len(requests)):
            u,v=requests[i]
            if u>v:
                u,v=v,u
            ui=find(u)
            vi=find(v)
            if ui==vi:
                ret[i]=True
            else:
                if vi in graph[ui] or ui in graph[vi]:
                    continue
                if disjoint[ui]>disjoint[vi]:
                    ui,vi=vi,ui
                for k in graph[vi].keys():
                    ki=find(k)
                    graph[ui][ki]=1
                    graph[ki][ui]=1
                disjoint[ui]+=disjoint[vi]
                disjoint[vi]=ui
                ret[i]=True
        return ret
                