class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        lst=[0]*(n+1)
        mask=1
        for i in range(16):
            if mask<len(lst):
                lst[mask]=1
            mask=mask<<1
        for i in range(1,len(lst)):
            lst[i]+=lst[i-1]
        if k>=n:
            return lst[n]
        ret=0
        while k>2 and n>0:
            if n%2:
                n=n//2
            else:
                n=n//2+1
            ret+=1
            if n==0:
                return ret
        import functools
        @functools.lru_cache(maxsize=None)
        def probe(num,rest):
            if rest==1:
                return num
            if num<=rest:
                return lst[num]
            ret=num
            for i in range(num):
                val0=probe(i,rest-1)
                val1=probe(num-i-1,rest)
                tmp=val0 if val0>val1 else val1
                tmp+=1
                if tmp<ret:
                    ret=tmp
            return ret
        return probe(n,k)