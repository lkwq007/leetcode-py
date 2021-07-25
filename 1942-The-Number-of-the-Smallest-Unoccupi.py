import heapq
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # 2 <= n <= 10^4
        idx=list(range(len(times)))
        idx.sort(key=lambda x: times[x][0])
        avail=list(range(len(times)))
        queue=[]
        chair=[0]*len(times)
        for item in idx:
            arrival,leaving=times[item]
            while queue and queue[0][0]<=arrival:
                _,pos=heapq.heappop(queue)
                heapq.heappush(avail,pos)
            pos=heapq.heappop(avail)
            if item==targetFriend:
                return pos
            heapq.heappush(queue,(leaving,pos))