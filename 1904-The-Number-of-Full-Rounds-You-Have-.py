import math
class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        if startTime==finishTime:
            return 0
        def calc(start,finish):
            func=lambda x: list(map(int,x.split(":")))
            hs,ms=func(start)
            hf,mf=func(finish)
            if hs==hf:
                return mf//15-math.ceil(ms/15)
            return mf//15+(60-ms)//15+4*(hf-hs-1)
        if startTime>finishTime:
            return calc("00:00",finishTime)+calc(startTime,"23:60")
        return calc(startTime,finishTime)