class Solution:
    def numWays(self, s: str) -> int:
        cnt=0
        term=10**9+7
        for item in s:
            if item=="1":
                cnt+=1
        ret=0
        if cnt==0:
            for i in range(1,len(s)-2+1):
                ret+=i
            return ret%term
        if cnt%3!=0:
            return 0
        idx=[]
        split0=cnt//3
        split1=2*split0
        cnt=0
        for i in range(len(s)):
            item=s[i]
            if item=="1":
                cnt+=1
            # faster than mod
                if cnt==split0:
                    idx.append(i)
                if cnt==split0+1:
                    idx.append(i)
                if cnt==split1:
                    idx.append(i)
                if cnt==split1+1:
                    idx.append(i)
        return ((idx[1]-idx[0])*(idx[3]-idx[2]))%term