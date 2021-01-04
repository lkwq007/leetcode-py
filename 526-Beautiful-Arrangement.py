class Solution:
    def countArrangement(self, N: int) -> int:
        # 1<=n<=15
        if N<4:
            return N
        template=list(range(N,0,-1))
        def probe(i,lst):
            if i==0:
                return 1
            tmp=list(lst)
            ret=0
            for idx,item in enumerate(lst,0):
                if item%i==0 or i%item==0:
                    tmp[idx],tmp[-1]=tmp[-1],tmp[idx]
                    ret+=probe(i-1,tuple(tmp[:-1]))
                    tmp[idx],tmp[-1]=tmp[-1],tmp[idx]
            return ret
        return probe(N,tuple(template))