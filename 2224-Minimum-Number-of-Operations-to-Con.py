class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        h0,m0=list(map(int,current.split(":")))
        h1,m1=list(map(int,correct.split(":")))
        ret=0
        if m1>=m0:
            ret+=h1-h0
        else:
            ret+=h1-h0-1
            m1+=60
        diff=m1-m0
        while diff>0:
            if diff>=15:
                ret+=1
                diff-=15
            elif diff>=5:
                ret+=1
                diff-=5
            else:
                ret+=diff
                diff=0
        return ret