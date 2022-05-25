class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort()
        lst=[0]*(len(nums))
        def update(x,val):
            while x<len(lst):
                lst[x]+=val
                x=x|(x+1)
        def add(start,end,val):
            update(start,val)
            update(end+1,-val)
        def query(x):
            ret=0
            while x>=0:
                ret+=lst[x]
                x=(x&(x+1))-1
            return ret
        for start,end in requests:
            add(start,end,1)
        idx=[query(i) for i in range(len(nums))]
        idx.sort()
        term=10**9+7
        ret=0
        for a,b in zip(nums,idx):
            ret+=a*b
            ret%=term
        return ret

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort()
        lst=[0]*(len(nums))
        for start,end in requests:
            lst[start]+=1
            if end+1<len(lst):
                lst[end+1]-=1
        for i in range(1,len(lst)):
            lst[i]+=lst[i-1]
        lst.sort()
        term=10**9+7
        ret=0
        for a,b in zip(nums,lst):
            ret+=a*b
            ret%=term
        return ret

