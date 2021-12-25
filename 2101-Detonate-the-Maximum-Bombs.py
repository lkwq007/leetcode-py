class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph=[[] for _ in range(len(bombs))]
        for i in range(len(bombs)):
            for j in range(i+1,len(bombs)):
                x0,y0,r0=bombs[i]
                x1,y1,r1=bombs[j]
                dist=(x0-x1)*(x0-x1)+(y0-y1)*(y0-y1)
                if dist<=r0*r0:
                    graph[i].append(j)
                if dist<=r1*r1:
                    graph[j].append(i)
        dp=[-1]*len(bombs)
        visited=[0]*len(bombs)
        def dfs(x):
            acc=1
            visited[x]=1
            for next in graph[x]:
                if not visited[next]:
                    acc+=dfs(next)
            return acc
        ret=0
        for i in range(len(bombs)):
            if dp[i]<0:
                ret=max(ret,dfs(i))
                visited=[0]*len(bombs)
        return ret
# class Solution:
#     def maximumDetonation(self, bombs: List[List[int]]) -> int:
#         # WA, note that not bidirectional
#         disjoint=[-1]*len(bombs)
#         def find(x):
#             idx=x
#             while disjoint[idx]>=0:
#                 idx=disjoint[idx]
#             while disjoint[x]>=0:
#                 next=disjoint[x]
#                 disjoint[x]=idx
#                 x=next
#             return idx
#         def union(a,b):
#             ai=find(a)
#             bi=find(b)
#             if ai==bi:
#                 return
#             if disjoint[ai]<disjoint[bi]:
#                 ai,bi=bi,ai
#             disjoint[ai]+=disjoint[bi]
#             disjoint[bi]=ai
#         for i in range(len(bombs)):
#             for j in range(i+1,len(bombs)):
#                 x0,y0,r0=bombs[i]
#                 x1,y1,r1=bombs[j]
#                 dist=(x0-x1)*(x0-x1)+(y0-y1)*(y0-y1)
#                 if dist<=r0*r0 or dist<=r1*r1:
#                     union(i,j)
#         return -min(disjoint)