class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        if len(arr)<1:
            return 0
        import functools
        @functools.lru_cache(maxsize=None)
        def probe(l,r):
            if l==r:
                return 0,arr[l]
            ret=-1
            max_val=0
            for i in range(l,r):
                lsum,lmax=probe(l,i)
                rsum,rmax=probe(i+1,r)
                if ret<0:
                    ret=lsum+rsum+lmax*rmax
                else:
                    ret=min(ret,lsum+rsum+lmax*rmax)
                max_val=max(max_val,lmax,rmax)
            return ret,max_val
        return probe(0,len(arr)-1)[0]