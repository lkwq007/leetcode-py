class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        min_height=n
        ret=[]
        graph=[[] for _ in range(n)]
        degree=[0]*n
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a]+=1
            degree[b]+=1
        queue=[]
        visited=[-1]*n
        for i in range(n):
            if degree[i]<=1:
                queue.append(i)
                degree[i]-=1
                visited[i]=0
        step=0
        while queue:
            target=[]
            step+=1
            for node in queue:
                for next in graph[node]:
                    degree[next]-=1
                    if visited[next]==-1 and degree[next]<=1:
                        visited[next]=step
                        target.append(next)
            if len(target)==0:
                return queue
            queue=target
        return queue

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # TLE
        min_height=n
        ret=[]
        graph=[[] for _ in range(n)]
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        def bfs(start):
            queue=[start]
            visited=[-1]*n
            visited[start]=0
            step=0
            while queue:
                target=[]
                step+=1
                for node in queue:
                    for next in graph[node]:
                        if visited[next]==-1:
                            visited[next]=step
                            target.append(next)
                queue=target
            return step
        for i in range(n):
            height=bfs(i)
            if height<min_height:
                min_height=height
                ret=[i]
            elif height==min_height:
                ret.append(i)
        return ret
