class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        template=[0]*(1+maxValue)
        dp=[template[:] for _ in range(20)]
        for i in range(1,maxValue+1):
            dp[1][i]=1
        last=1
        record=[0]*20
        for i in range(1,20):
            acc=0
            for j in range(last,maxValue+1):
                for k in range(2,(maxValue//j)+1):
                    next=j*k
                    dp[i+1][next]+=dp[i][j]
                acc+=dp[i][j]
            record[i]=acc
            last=last*2
        term=10**9+7
        ret=record[1]
        total=n
        last=1
        for i in range(2,len(record)):
            if record[i]>0 and i<=n:
                cur=(last*(total-i+1))%term
                cur=cur*pow(i-1,-1,term)
                ret+=record[i]*cur
                ret%=term
                last=cur
        return ret

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        record=[0]*20
        def dfs(x,acc):
            val=2
            record[acc]+=1
            while True:
                cur=x*val
                if cur<=maxValue:
                    dfs(cur,acc+1)
                else:
                    break
                val+=1
        for i in range(1,maxValue+1):
            dfs(i,1)
        term=10**9+7
        def probe(total,x):
            a=total-1
            b=x-1
            acc=1
            for i in range(b):
                acc*=a
                acc%=term
                a-=1
            for i in range(2,b+1):
                acc=acc*pow(i,-1,term)
            return acc%term
        ret=0
        for i in range(len(record)):
            if record[i]>0 and i<=n:
                ret+=record[i]*probe(n,i)
                ret%=term
        return ret