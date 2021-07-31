class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        ret=[1]
        while len(ret)<n:
            lst=[]
            for item in ret:
                if item*2-1<=n:
                    lst.append(item*2-1)
            for item in lst:
                if item*2<=n:
                    lst.append(item*2)
            ret=lst
        return ret
