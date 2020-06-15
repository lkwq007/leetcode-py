from typing import List

import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=list(map(lambda x:-x,stones))
        heapq.heapify(heap)
        while len(heap)>1:
            x=heapq.heappop(heap)
            y=heapq.heappop(heap)
            if x==y:
                continue
            else:
                x=-x
                y=-y
                res=x-y if x>y else y-x
                heapq.heappush(heap,-res)
        if len(heap)==1:
            return -heap[0]
        else:
            return 0

x=Solution()
print(x.lastStoneWeight([2,7,4,1,8,1]))