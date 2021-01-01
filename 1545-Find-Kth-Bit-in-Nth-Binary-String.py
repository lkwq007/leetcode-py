class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n<2:
            return "0"
        acc=1
        for i in range(n-1):
            acc=2*acc+1
        def probe(i,k,total,opt):
            if i==1:
                return "0" if opt%2==0 else "1"
            if total//2==k:
                return "1" if opt%2==0 else "0"
            if k<total//2:
                return probe(i-1,k,total//2,opt)
            else:
                return probe(i-1,total-k-1,total//2,opt+1)
        return probe(n,k-1,acc,0)