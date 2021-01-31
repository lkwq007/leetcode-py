class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph={}
        for a,b in adjacentPairs:
            if a not in graph:
                graph[a]=[]
            if b not in graph:
                graph[b]=[]
            graph[a].append(b)
            graph[b].append(a)
        self.lst=[]
        def dfs(x,p=None):
            self.lst.append(x)
            for next in graph[x]:
                if next!=p:
                    dfs(next,x)
        for k,v in graph.items():
            if len(v)==1:
                dfs(k)
                break
        return self.lst