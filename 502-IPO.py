class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        cheap=[]
        pheap=[(-p,c) for p,c in zip(profits,capital)]
        import heapq
        heapq.heapify(pheap)
        while k>0 and pheap:
            top=heapq.heappop(pheap)
            p,c=-top[0],top[1]
            if w>=c:
                w+=p
                k-=1
            else:
                heapq.heappush(cheap,(c,-p))
            while cheap and cheap[0][0]<=w:
                top=heapq.heappop(cheap)
                heapq.heappush(pheap,(top[1],top[0]))
        return w