class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if duration<1 or len(timeSeries)<1:
            return 0
        ret=0
        last=len(timeSeries)-1
        for i in range(len(timeSeries)):
            if i==last:
                ret+=duration
            else:
                ret+=min(duration,timeSeries[i+1]-timeSeries[i])
        return ret
