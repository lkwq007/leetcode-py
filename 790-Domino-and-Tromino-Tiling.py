class Solution:
    def numTilings(self, n: int) -> int:
        if n<3:
            return n
        term=10**9+7
        EMPTY=0
        UP=1
        DOWN=2
        FULL=3
        # 4 states, empty, UP, BOTTOM, full
        last=[1,1,1,2]
        for i in range(3,n+1):
            cur=[0]*4
            cur[EMPTY]=last[FULL]%term
            cur[UP]=(last[DOWN]+last[EMPTY])%term
            cur[DOWN]=(last[UP]+last[EMPTY])%term
            cur[FULL]=(last[FULL]+last[UP]+last[DOWN]+last[EMPTY])%term
            last=cur
        return last[-1]
