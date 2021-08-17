class Solution:
    def lastRemaining(self, n: int) -> int:
        cnt=0
        while n>0:
            n=n//2
            cnt+=1
        ret=0
        offset=1
        for i in range(cnt):
            ret*=2
            ret+=offset
            offset=1-offset
        cur=1
        lst=list(range(1,10))
        next=[]
        while len(lst)>2:
            for item in lst:
                
        return ret