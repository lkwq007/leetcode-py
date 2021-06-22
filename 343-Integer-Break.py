import functools
class Solution:
    def integerBreak(self, n: int) -> int:
        @functools.lru_cache(maxsize=None)
        def probe(x):
            ret=x
            for i in range(x//2):
                val=i+1
                ret=max(ret,val*probe(x-val))
            return ret
        acc=0
        for i in range(1,n//2+1):
            acc=max(acc,i*probe(n-i))
        return acc

import functools
class Solution:
    def integerBreak(self, n: int) -> int:
        @functools.lru_cache(maxsize=None)
        def probe(x,flag=False):
            ret=0 if flag else x
            for i in range(x//2):
                val=i+1
                ret=max(ret,val*probe(x-val))
            return ret
        return probe(n,True)