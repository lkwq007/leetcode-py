class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n>45 or n<1:
            return []
        ret=[]
        def probe(i,rest,lst):
            if i==k-1:
                if rest not in lst and 1<=rest<=9:
                    if lst and rest<=lst[-1]:
                        return
                    lst.append(rest)
                    ret.append(lst[:])
                    lst.pop()
                return
            start=lst[-1]+1 if lst else 1
            for idx in range(start,10):
                if rest>idx and rest-idx>idx:
                    lst.append(idx)
                    probe(i+1,rest-idx,lst)
                    lst.pop()
        probe(0,n,[])
        return ret
