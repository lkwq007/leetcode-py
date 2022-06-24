class Solution:
    def queryString(self, s: str, n: int) -> bool:
        total=0
        x=n
        while x>0:
            total+=1
            x=x>>1
        slst=list(map(int,s))
        record=set([])
        lst=[0]*len(s)
        for l in range(total):
            for i in range(len(s)):
                if slst[i]==1:
                    if i+l<len(s):
                        cur=lst[i]*2+slst[i+l]
                        lst[i]=cur
                        if cur<=n:
                            record.add(cur)
        return len(record)==n