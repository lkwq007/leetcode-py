class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        total=len(points)
        dist=[[0]*total for _ in range(total)]
        for i in range(total):
            for j in range(i+1,total):
                d=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                dist[i][j]=d
                dist[j][i]=d