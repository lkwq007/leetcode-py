class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if len(dislikes)<1 or N<2:
            return True
        graph={}
        for a,b in dislikes:
            if a in graph:
                graph[a].append(b)
            else:
                graph[a]=[b]
            if b in graph:
                graph[b].append(a)
            else:
                graph[b]=[a]
        record=[-1]*(N+1)
        self.flag=False
        def dfs(node,val):
            if record[node]<0:
                record[node]=val
                for item in graph[node]:
                    dfs(item,1-val)
            elif record[node]!=val:
                self.flag=True
            return

        for idx in range(1,N+1):
            if record[idx]<0 and idx in graph:
                dfs(idx,0)
            if self.flag:
                return False
        return True