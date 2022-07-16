class Solution:
    def fillCups(self, amount: List[int]) -> int:
        import heapq
        lst=[-item for item in amount]
        lst.sort()
        ret=0
        while len(lst)>0:
            if len(lst)<3:
                return ret-min(lst)
            top=-heapq.heappop(lst)
            second=-heapq.heappop(lst)
            if second>0:
                diff=second-max(-lst[0]-1,0)
                second-=diff
                ret+=diff
                top-=diff
            if second>0:
                heapq.heappush(lst,-second)
            if top>0:
                heapq.heappush(lst,-top)
        return ret