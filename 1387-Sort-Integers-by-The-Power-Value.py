class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # even x=x>>1
        # odd x=2*x+x+1, next: x+(x+1)>>1
        record={}
        record[1]=0
        def power(x):
            if record.get(x,0)==0 and x!=1:
                if x%2:
                    ret=power(3*x+1)
                else:
                    ret=power(x//2)
                record[x]=1+ret
            return record[x]
        ret=list(range(lo,hi+1))
        for i in range(2,hi+1):
            tmp=power(i)
        ret.sort(key=lambda x: (record[x],x))
        return ret[k-1]
