class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start==distance:
            return 0
        total=sum(distance)
        dist=0
        for i in range(min(start,destination),max(start,destination)):
            dist+=distance[i]
        return min(dist,total-dist)