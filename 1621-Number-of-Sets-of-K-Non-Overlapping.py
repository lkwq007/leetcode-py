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
                ret+=(idx-start)*probe(num-1,idx)
                ret%=term
            return ret
        return probe(k,1)

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        term=10**9+7
        def calc(n,i):
            ret=1
            for i in range(i+1,n+1):
                ret*=n
                ret%=term
            return ret
        return calc(n,k+1)