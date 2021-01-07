import functools
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        term=10**9+7
        @functools.lru_cache(maxsize=None)
        def probe(num,start):
            total=n-start+1
            if num<1 or num>=total:
                return 0
            if num+1==total:
                return 1
            if num==1:
                return total*(total-1)//2
            ret=0
            for idx in range(start+1,n+1):
                if num-1>=n-idx+1:
                    break
                ret+=(idx-start)*probe(num-1,idx)
                ret%=term
            return ret
        return probe(k,1)

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        term=10**9+7
        def calc(n,i):
            if i==0 or n==i:
                return 1
            if n<i:
                return 0
            k=min(i,n-i)
            ret=1
            for idx in range(k):
                ret*=(n-idx)//(idx+1)
                ret%=term
            return ret
        # total segments
        total=0
        for i in range(k+1,2*k+1):
            print(calc(n,k+1))
            total+=calc(n,i)*calc(i,i-k-1)
            total%=term
        return total