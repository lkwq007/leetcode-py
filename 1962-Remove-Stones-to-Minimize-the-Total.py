import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        lst=[-x for x in piles]
        heapq.heapify(lst)
        total=sum(piles)
        ret=0
        for i in range(k):
            cur=heapq.heappop(lst)
            half=-cur//2
            ret+=half
            heapq.heappush(lst,cur+half)
        return total-ret
