class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        total=len(points)
        dist=[[0]*total for _ in range(total)]
        for i in range(total):
            for j in range(i+1,total):
                d=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                dist[i][j]=d
                dist[j][i]=d
        visited=[False]*total
        min_idx=[dist[0][i] for i in range(total)]
        ret=0
        for i in range(total):
            idx=-1
            for j in range(total):
                if not visited[j] and (idx==-1 or min_idx[j]<min_idx[idx]):
                    idx=j
            visited[idx]=True
            ret+=min_idx[idx]
            for j in range(total):
                if dist[idx][j]<min_idx[j]:
                    min_idx[j]=dist[idx][j]
        return ret