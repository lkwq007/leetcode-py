class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        ret=abs(start[0]-target[0])+abs(start[1]-target[1])
        import heapq
        def test(item):
            dist=abs(item[0]-item[2])+abs(item[1]-item[3])
            return dist>item[-1]
        specialRoads=list(filter(test,specialRoads))
        import heapq
        dist={}
        heap=[(0,start[0],start[1])]
        dist[tuple(start)]=0
        while heap:
            d,x,y=heapq.heappop(heap)
            if d!=dist.get((x,y),-1):
                continue
            for x1,y1,x2,y2,cost in specialRoads:
                cur=abs(x-x1)+abs(y-y1)+cost+d
                if cur>ret:
                    continue
                d_next=dist.get((x2,y2),-1)
                if d_next==-1 or cur<d_next:
                    heapq.heappush(heap,(cur,x2,y2))
                    dist[(x2,y2)]=cur
                    ret=min(ret,cur+abs(target[0]-x2)+abs(target[1]-y2))
        return ret
