class Solution:
    def largestVariance(self, s: str) -> int:
        # remove if, max
        lst=set(list(s))
        full=(1<<16)-1
        def probe(a,b):
            if a==b:
                return 0
            ret=0
            acc=0
            left=0
            mask=0
            for item in s:
                if item==a:
                    if acc>=0:
                        acc+=1
                    else:
                        acc=1
                    cur=(acc-left)&mask
                    if cur>ret:
                        ret=cur
                    # ret=max(ret,(acc-left)&mask)
                elif item==b:
                    if acc>0:
                        left=0
                    else:
                        left=1
                    acc-=1
                    mask=full
                    cur=acc-left
                    if cur>ret:
                        ret=cur
                    # ret=max(ret,acc-left)
            return ret
        val=0
        for i in lst:
            for j in lst:
                val=max(probe(i,j),val)
        return val

class Solution:
    def largestVariance(self, s: str) -> int:
        # pass
        lst=set(list(s))
        def probe(a,b):
            if a==b:
                return 0
            ret=0
            acc=0
            left=0
            flag=False
            for item in s:
                if item==a:
                    if acc>=0:
                        acc+=1
                    else:
                        acc=1
                    if flag:
                        ret=max(ret,acc-left)
                elif item==b:
                    if acc>0:
                        acc-=1
                        left=0
                    else:
                        acc=-1
                        left=1
                    flag=True
                    ret=max(ret,acc-left)
            return ret
        val=0
        for i in lst:
            for j in lst:
                val=max(probe(i,j),val)
        return val

class Solution:
    def largestVariance(self, s: str) -> int:
        # pass by chance
        lst=set(list(s))
        def probe(a,b):
            if a==b:
                return 0
            ret=0
            acc=0
            left=False
            flag=False
            for item in s:
                if item==a:
                    if acc>=0:
                        acc+=1
                    else:
                        acc=1
                elif item==b:
                    if acc>0:
                        acc-=1
                        left=False
                    else:
                        acc=-1
                        left=True
                    flag=True
                if flag:
                    if left:
                        ret=max(ret,acc-1)
                    else:
                        ret=max(ret,acc)
            return ret
        val=0
        for i in lst:
            for j in lst:
                val=max(probe(i,j),val)
        return val

class Solution:
    def largestVariance(self, s: str) -> int:
        # TLE
        template=[0]*(len(s)+1)
        prefix=[template[:] for _ in range(26)]
        base=ord("a")
        for i in range(len(s)):
            for j in range(26):
                prefix[j][i]=prefix[j][i-1]
            cur=ord(s[i])-base
            prefix[cur][i]+=1
        ret=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                min_val=len(s)
                max_val=-1
                for k in range(26):
                    cur=prefix[k][j]-prefix[k][i-1]
                    if cur>0:
                        min_val=min(cur,min_val)
                        max_val=max(cur,max_val)
                ret=max(ret,max_val-min_val)
        return ret

