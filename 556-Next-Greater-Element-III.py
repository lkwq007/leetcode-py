class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if n<=11:
            return -1
        lst=[int(item) for item in str(n)]
        def convert(x):
            acc=0
            for item in x:
                acc=acc*10+item
            return acc
        def probe(i):
            if i<0:
                return -1
            if lst[i]>=lst[i+1]:
                return probe(i-1)
            idx=-1
            while lst[idx]<=lst[i]:
                idx-=1
            lst[i],lst[idx]=lst[idx],lst[i]
            
            return convert(lst[:i+1]+sorted(lst[i+1:]))
        ret=probe(len(lst)-2)
        if ret>(2**31-1):
            return -1
        return ret