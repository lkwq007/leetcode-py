import heapq
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total=sum(nums)
        lst=[-x for x in nums]
        heapq.heapify(lst)
        target=total/2
        ret=0
        acc=0
        while acc<target:
            top=heapq.heappop(lst)
            acc-=top/2
            heapq.heappush(lst,top/2)
            ret+=1
        return ret

