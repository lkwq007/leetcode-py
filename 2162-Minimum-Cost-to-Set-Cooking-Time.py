class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def calc(lst):
            last=startAt
            acc=0
            for item in lst:
                if item!=last:
                    acc+=moveCost
                acc+=pushCost
                last=item
            return acc
        minute=targetSeconds//60
        second=targetSeconds%60
        convert=lambda x: list(map(int,str(x)))
        ret=99999999
        if minute==0:
            return calc(convert(second))
        elif second+60<=99:
            if minute-1==0:
                ret=min(ret,calc(convert(second+60)))
            else:
                ret=min(ret,calc(convert(minute-1)+convert(second+60)))
        if minute<=99:
            mid=[] if second>9 else [0]
            ret=min(ret,calc(convert(minute)+mid+convert(second)))
        return ret