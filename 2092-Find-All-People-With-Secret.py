class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        record=[0]*n
        record[firstPerson]=1
        meetings.sort(key=lambda x:x[-1])
        cur=0
        pool=[]
        def process(lst):
            graph={}
            visited={}
            for x,y in lst:
                if x not in graph:
                    graph[x]=[]
                if y not in graph:
                    graph[y]=[]
                graph[x].append(y)
                graph[y].append(x)
            def dfs(idx):
                visited[idx]=1
                for next in graph[idx]:
                    if next not in visited:
                        record[next]=1
                        dfs(next)
            for k in graph.keys():
                if record[k]==1 and k not in visited:
                    dfs(k)
        for x,y,t in meetings:
            if cur!=t:
                process(pool)
                cur=t
            else:
                pool.append((x,y))
        process(pool)
        return [i for i in range(n) if record[i]==1]