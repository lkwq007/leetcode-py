import heapq
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        # max second, min first
        n=len(nums)//3
        acc=0
        heap=[]
        for i in range(n):
            acc+=nums[i]
            heap.append(-nums[i])
        heapq.heapify(heap)
        record={}
        lst=[]
        for i in range(n,len(nums)):
            item=nums[i]
            lst.append(item)
        lst.sort()
        heap1=[-item for item in lst[:n]]
        for item in heap1:
            record[-item]=record.get(-item,0)+1
        heap2=lst[n:]
        lacc=acc
        racc=sum(heap2)
        heapq.heapify(heap1)
        heapq.heapify(heap2)
        ret=lacc-racc
        # print(sum(nums[2*n:]),len(nums[2*n:]))
        for i in range(n,len(nums)-n):
            # left part
            cur=nums[i]
            heapq.heappush(heap,-cur)
            top=heapq.heappop(heap)
            lacc=lacc+cur+top
            # right
            if cur>=heap2[0]:
                while heap1 and record[-heap1[0]]==0:
                    heapq.heappop(heap1)
                top=-heapq.heappop(heap1)
                racc=racc-cur+top
                heapq.heappush(heap2,top)
                record[top]-=1
            else:
                record[cur]-=1
            # print(record,heap1,heap2)
            # print(cur,ret,lacc-racc,lacc,racc)
            # print(sum(list(sorted(nums[i+1:]))[-n:]))
            ret=min(ret,lacc-racc)
        return ret
            