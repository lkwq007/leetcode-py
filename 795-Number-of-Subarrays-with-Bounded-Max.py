class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        ret=0
        acc=0
        cnt=0
        for item in A:
            if item>R:
                acc=0
                cnt=0
            elif item>=L:
                acc+=1
                cnt=0
            else:
                cnt+=1
                acc+=1
            ret+=acc-cnt
        return ret

import functools
class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        return functools.reduce(lambda x,y: (x[0],0,0) if y>R else ((x[0]+x[1]+1,x[1]+1,0) if y>=L else (x[0]+x[1]-x[2],x[1]+1,x[2]+1)),A,(0,0,0))[0]