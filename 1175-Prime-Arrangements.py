class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def is_prime(x):
            if x<2:
                return False
            if x<4:
                return True
            i=2
            while i*i<=x:
                if x%i==0:
                    return False
                i+=1
            return True
        cnt=0
        for i in range(2,n+1):
            if is_prime(i):
                cnt+=1
        term=10**9+7
        def calc(x):
            acc=1
            for i in range(2,x+1):
                acc=(acc*i)%term
            return acc
        return (calc(cnt)*calc(n-cnt))%term
