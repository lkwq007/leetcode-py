class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        lst=[0]*(24*60)
        last=0
        for item in timePoints:
            hour=int(item[:2])
            minute=int(item[3:])
            cur=hour*60+minute
            lst[cur]+=1
            last=max(last,cur)
        ret=24*60
        last-=ret
        for i in range(len(lst)):
            if lst[i]>1:
                return 0
            elif lst[i]==1:
                ret=min(ret,i-last)
                last=i
        return ret