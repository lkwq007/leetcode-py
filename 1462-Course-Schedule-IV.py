class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # n courses
        tin=[0]*n
        tout=[0]*n
        visited=[False]*n
        timer=1
        graph=[[] for i in range(n)]
        for prep,cur in prerequisites:
            graph[prep].append(cur)
        def dfs(u):
            visited[u]=True
            tin=timer
            timer+=1
            for v in graph[u]:
                if not visited[v]:
                    dfs(v)
        for i in range(n):
            if not visited[i]:
                dfs(i)