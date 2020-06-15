class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # undirected tree
        total=len(hasApple)
        graph=[None]*total
        for idx in range(0,total):
            graph[idx]={}
        for v0,v1 in edges:
            graph[v0][v1]=1
            graph[v1][v0]=1
        # root is 0
        self.total=0
        def dfs(node):
            keys=list(graph[node].keys())
            cnt=0
            if len(keys)>0:
                for item in keys:
                    del graph[item][node]
                    flag=dfs(item)
                    if not flag:
                        del graph[node][item]
                    else:
                        cnt+=1
            ret=False
            if hasApple[node] or cnt>0:
                ret=True
                self.total+=1
            return ret
        dfs(0)
        return (self.total-1)*2 if self.total>0 else 0