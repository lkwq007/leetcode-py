class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        cnt=0
        step=1+(n%2)
        for i in range(1,n+1,step):
            if n%i==0:
                cnt+=1
                if cnt==k:
                    return i
        return -1

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        i=1
        while i*i<=n:
            if n%i==0:
                k-=1
                if k==0:
                    return i
            i+=1
        i-=1
        if i*i==n:
            i-=1
        while i>0:
            if n%i==0:
                k-=1
                if k==0:
                    return n//i
            i-=1
        return -1
