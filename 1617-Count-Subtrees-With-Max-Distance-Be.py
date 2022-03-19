class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        # 2 <= n <= 15
        # len(edges) == n-1
        ret=[0]*(n-1)
        graph=[[] for _ in range(n)]
        for u,v in graph:
            graph[u].append(v)
            graph[v].append(u)
        ret[0]=n-1
        