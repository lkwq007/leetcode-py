class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        # build edges
        ret=-1
        graph=[[] for _ in range(len(scores))]
        for u,v in edges:
            val=scores[u]+scores[v]
            graph[u].append((-val,v))
            graph[v].append((-val,u))
        for i in range(len(graph)):
            graph[i].sort()
        def probe(u,v,idx1=0,idx2=0):
            if idx1>=len(graph[u]) or idx2>=len(graph[v]):
                return -1
            while idx1<len(graph[u]) and idx2<len(graph[v]):
                if graph[u][idx1][1]==v:
                    idx1+=1
                    continue
                if graph[v][idx2][1]==u:
                    idx2+=1
                    continue
                if graph[u][idx1][1]==graph[v][idx2][1]:
                    return max(probe(u,v,idx1+1,idx2),probe(u,v,idx1,idx2+1))
                return -graph[u][idx1][0]-graph[v][idx2][0]
            return -1
        for u,v in edges:
            ret=max(ret,probe(u,v,0,0))
        return ret
        

# class Solution:
#     def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
#         self.ret=-1
#         # brute force? TLE
#         graph=[[] for _ in range(len(scores))]
#         for u,v in edges:
#             graph[u].append(v)
#             graph[v].append(u)
#         # brute force?
#         visited=[0]*len(scores)
#         def dfs(x,level,acc):
#             visited[x]=1
#             if level==3:
#                 self.ret=max(self.ret,acc+scores[x])
#                 visited[x]=0
#                 return
#             for next in graph[x]:
#                 if visited[next]==0:
#                     dfs(next,level+1,acc+scores[x])
#             visited[x]=0
#             return
#         for i in range(len(scores)):
#             dfs(i,0,0)
#         return self.ret