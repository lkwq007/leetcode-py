class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        ret=[0]*n
        graph=[[] for _ in range(n)]
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        ret=[0]*n
        base=ord("a")
        def dfs(x,p):
            cur=[0]*26
            cur[ord(labels[x])-base]=1
            for child in graph[x]:
                if child==p:
                    continue
                lst=dfs(child,x)
                for i in range(26):
                    cur[i]+=lst[i]
            ret[x]=cur[ord(labels[x])-base]
            return cur
        dfs(0,-1)
        return ret
