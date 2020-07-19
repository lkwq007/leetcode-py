from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ret=[]
        template=[0]*k
        def comb(pos,cnt,lst):
            if cnt==k:
                self.ret.append(lst[:])
                return
            if pos>n:
                return
            lst[cnt]=pos
            comb(pos+1,cnt+1,lst)
            comb(pos+1,cnt,lst)
        comb(1,0,template)
        return self.ret
x=Solution()
print(x.combine(4,0))