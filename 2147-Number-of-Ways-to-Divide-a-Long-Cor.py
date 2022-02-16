class Solution:
    def numberOfWays(self, corridor: str) -> int:
        cnt=0
        term=10**9+7
        for item in corridor:
            if item=="S":
                cnt+=1
        if cnt<1 or cnt%2:
            return 0
        ret=1
        i=0
        while i<len(corridor) and cnt>0:
            acc=0
            while acc<2:
                if corridor[i]=="S":
                    acc+=1
                i+=1
            cnt-=2
            cur=1
            while cnt>0 and corridor[i]!="S":
                cur+=1
                i+=1
            ret=(ret*cur)%term
        return ret