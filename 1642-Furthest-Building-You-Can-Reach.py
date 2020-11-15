import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pos=0
        heap=[]
        while pos<len(heights)-1:
            if heights[pos]>=heights[pos+1]:
                pos+=1
            else:
                diff=heights[pos+1]-heights[pos]
                if ladders>0:
                    heapq.heappush(heap,diff)
                    ladders-=1
                elif len(heap)>0 and heap[0]<diff:
                    ret=heapq.heapreplace(heap,diff)
                    bricks-=ret
                    if bricks<0:
                        return pos
                else:
                    if bricks<diff:
                        return pos
                    else:
                        bricks-=diff
                pos+=1
        return pos
