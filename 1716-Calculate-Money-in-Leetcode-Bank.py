class Solution:
    def totalMoney(self, n: int) -> int:
        n-=1
        weeks=n//7
        rest=n%7
        lastweek=(1+weeks+1+weeks+rest)*(rest+1)//2
        base=7*weeks*(0+weeks-1)//2+(1+7)//2*7*weeks
        return lastweek+base