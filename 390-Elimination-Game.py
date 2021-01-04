class Solution:
    def lastRemaining(self, n: int) -> int:
        cnt=0
        while n>0:
            n=n//2
            cnt+=1
        ret=1
        for i in range(cnt):
            if cnt%2==0:
                
        if cnt%2==1:
            return (n+1)//2+1
        else:
            return (n+1)//2