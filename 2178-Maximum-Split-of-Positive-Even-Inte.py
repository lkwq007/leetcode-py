class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum%2:
            return []
        # greedy?
        cur=2
        ret=[]
        while finalSum>=cur:
            rest=finalSum-cur
            if rest<=cur:
                ret.append(finalSum)
                break
            ret.append(cur)
            cur+=2
            finalSum=rest
        return ret