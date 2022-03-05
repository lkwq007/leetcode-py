import functools
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        # topo sort or just dfs?
        graph={}
        for a,b in edges:
            if a not in graph:
                graph[a]=[]
            graph[a].append(b)
        visited=[0]*len(colors)
        # is a child an ancestor 
        def check(x):
            visited[x]=1
            for next in graph.get(x,[]):
                if visited[next]==0:
                    if check(next):
                        return True
                if visited[next]==1:
                    return True
            visited[x]=2
            return False
        for i in range(len(colors)):
            if check(i):
                return -1
        # no cycle
        self.ret=0
        visited=[0]*len(colors)
        @functools.lru_cache(maxsize=None)
        def dfs(x):
            ret=[0]*26
            cur=ord(colors[x])-ord("a")
            for next in graph.get(x,[]):
                stat=dfs(next)
                for i in range(26):
                    ret[i]=max(stat[i],ret[i])
            ret[cur]+=1
            return tuple(ret)
        for i in range(len(colors)):
            self.ret=max(max(dfs(i)),self.ret)
        return self.ret