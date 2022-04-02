class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        ret=[0]*len(queries)
        items.sort()
        for i in range(1,len(items)):
            items[i][1]=max(items[i-1][1],items[i][1])
        lst=[(queries[i],i) for i in range(len(queries))]
        lst.sort()
        idx=0
        last=0
        for q,i in lst:
            while idx<len(items) and items[idx][0]<=q:
                last=items[idx][1]
                idx+=1
            ret[i]=last
        return ret

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        ret=[0]*len(queries)
        record={}
        acc=0
        items.sort()
        for p,b in items:
            acc=max(acc,b)
            record[p]=acc
        lst=[(k,v) for k,v in record.items()]
        for i in range(len(queries)):
            q=queries[i]
            if q in record:
                ret[i]=record[q]
            else:
                left=0
                right=len(lst)-1
                while left<right:
                    middle=left+(right-left)//2
                    if lst[middle][0]<q:
                        left=middle+1
                    else:
                        right=middle
                if lst[left][0]>q:
                    left-=1
                if left>=0:
                    ret[i]=lst[left][1]
        return ret