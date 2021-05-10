import heapq
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        # all positive
        queue=[-x for x in target]
        heapq.heapify(queue)
        total=-sum(queue)
        cnt=0
        # rest + val0 = S0
        # rest + val0 + rest = S1
        # rest + S1 = S2
        while True:
            top=-heapq.heappop(queue)
            if top==1:
                return True
            rest=total-top
            cur=top+top-total
            if cur<1 or rest<1:
                return False
            cur=total%rest
            next=-queue[0]
            total=rest+cur
            cnt+=1
            heapq.heappush(queue,-cur)
        return True