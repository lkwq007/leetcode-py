class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        term=10**9+7
        # 1 <= nums.length, k <= 105
        if len(nums)==1:
            return nums[0]+k
        record={}
        for item in nums:
            record[item]=record.get(item,0)+1
        lst=[(key,v) for key,v in record.items()]            
        import heapq
        heapq.heapify(lst)
        while k>0:
            key,val=heapq.heappop(lst)
            if lst:
                key1=lst[0][0]
                diff=key1-key
                total=diff*val
                total=min(k,total)                    
                k-=total
                x=total//val
                r=total%val
                if r>0:
                    if key+x+1==key1:
                        lst[0]=(key1,lst[0][1]+r)
                    else:
                        heapq.heappush(lst,(key+x+1,r))
                if key+x==key1:
                    lst[0]=(key1,lst[0][1]+val-r)
                else:
                    heapq.heappush(lst,(key+x,val-r))
            else:
                x=k//val
                r=k%val
                if r>0:
                    heapq.heappush(lst,(key+x+1,r))
                heapq.heappush(lst,(key+x,val-r))
                k=0
        ret=1
        for key,val in lst:
            for i in range(val):
                ret*=key
                ret%=term
        return ret
