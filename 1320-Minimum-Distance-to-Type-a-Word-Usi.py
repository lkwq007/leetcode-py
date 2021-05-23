class Solution:
    def minimumDistance(self, word: str) -> int:
        template=[-1]*27
        dp=[template[:] for _ in range(len(word))]
        base=ord("A")-1
        dp[0][0]=0        
        def pos(x):
            idx=ord(x)-base-1
            y=idx//6
            x=idx%6
            return y,x
        def distance(a,b):
            y0,x0=pos(a)
            y1,x1=pos(b)
            return abs(y0-y1)+abs(x0-x1)
        for i in range(1,len(word)):
            dp[i][0]=dp[i-1][0]+distance(word[i],word[i-1])
            cur=ord(word[i])-base
            last=ord(word[i-1])-base
            for j in range(1,27):
                if dp[i-1][j]>=0:
                    dp[i][j]=dp[i-1][j]+distance(word[i],word[i-1])
            # if dp[i][cur]<1:
            #     dp[i][cur]=dp[i-1][0]
            # else:
            #     dp[i][cur]=min(dp[i-1][0],dp[i][cur])
            dp[i][last]=dp[i-1][0]
            for j in range(1,27):
                if dp[i-1][j]>=0:
                    dp[i][last]=min(dp[i][last],dp[i-1][j]+distance(chr(j+base),word[i]))
        return min([item for item in dp[-1] if item>=0])