class Solution:
    def distinctSequences(self, n: int) -> int:
        if n==1:
            return 6
        mapping=[list(range(2,7)),[1,3,5],[1,2,4,5],[1,3,5],[1,2,3,4,6],[1,5]]
        queue=[[i] for i in range(6)]
        for i in range(min(2,n-1)):
            target=[]
            for lst in queue:
                for adj in mapping[lst[-1]]:
                    val=adj-1
                    if len(lst)>1 and lst[-2]==val:
                        continue
                    target.append((*lst,val))
            queue=target
        if n<=3:
            return len(queue)
        record={}
        for i,item in enumerate(queue):
            record[item]=i
        idx=[[] for _ in range(len(queue))]
        last=[1]*len(queue)
        # print(queue)
        for i,lst in enumerate(queue):
            for adj in mapping[lst[-1]]:
                val=adj-1
                if lst[-2]==val:
                    continue
                cur=(*lst[1:],val)
                idx[i].append(record[cur])
        term=10**9+7
        dp=[0]*len(queue)
        for i in range(3,n):
            for j in range(len(queue)):
                dp[j]=0
                for next in idx[j]:
                    dp[j]+=last[next]
                dp[j]%=term
            last,dp=dp,last
        return sum(last)%term

class Solution:
    def distinctSequences(self, n: int) -> int:
        if n==1:
            return 6
        mapping=[list(range(2,7)),[1,3,5],[1,2,4,5],[1,3,5],[1,2,3,4,6],[1,5]]
        dp=[[0]*6 for _ in range(n)]
        term=10**9+7
        for i in range(6):
            dp[0][i]=1
        for i in range(6):
            dp[1][i]=0
            for adj in mapping[i]:
                dp[1][i]+=dp[0][adj-1]
        for i in range(2,n):
            cur=i
            last=(i-1)
            last2=(i-2)
            for j in range(6):
                dp[cur][j]=0
                for adj in mapping[j]:
                    val=adj-1
                    dp[cur][j]+=dp[last][val]-dp[last2][j]
                    dp[cur][j]%=term
        return sum(dp[(n-1)])%term