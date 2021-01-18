
class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        # better dp
        dp=[[N]*N for _ in range(N)]
        for y,x in mines:
            dp[y][x]=0
        for y in range(N):
            acc=1
            for x in range(N):
                dp[y][x]=min(acc,dp[y][x])
                if dp[y][x]==0:
                    acc=1
                else:
                    acc+=1
            acc=1
            for x in range(N-1,-1,-1):
                dp[y][x]=min(acc,dp[y][x])
                if dp[y][x]==0:
                    acc=1
                else:
                    acc+=1
        for x in range(N):
            acc=1
            for y in range(N):
                dp[y][x]=min(acc,dp[y][x])
                if dp[y][x]==0:
                    acc=1
                else:
                    acc+=1
            acc=1
            for y in range(N-1,-1,-1):
                dp[y][x]=min(acc,dp[y][x])
                if dp[y][x]==0:
                    acc=1
                else:
                    acc+=1
        ret=0
        for y in range(N):
            for x in range(N):
                ret=max(ret,dp[y][x])
        return ret

class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        # dp
        record={}
        for y,x in mines:
            record[(y,x)]=1
        dp=[[N]*N for _ in range(N)]
        for y in range(N):
            acc=1
            for x in range(N):
                if (y,x) in record:
                    dp[y][x]=0
                    acc=1
                else:
                    dp[y][x]=min(acc,dp[y][x])
                    acc+=1
            acc=1
            for x in range(N-1,-1,-1):
                if (y,x) in record:
                    dp[y][x]=0
                    acc=1
                else:
                    dp[y][x]=min(acc,dp[y][x])
                    acc+=1
        for x in range(N):
            acc=1
            for y in range(N):
                if (y,x) in record:
                    dp[y][x]=0
                    acc=1
                else:
                    dp[y][x]=min(acc,dp[y][x])
                    acc+=1
            acc=1
            for y in range(N-1,-1,-1):
                if (y,x) in record:
                    dp[y][x]=0
                    acc=1
                else:
                    dp[y][x]=min(acc,dp[y][x])
                    acc+=1
        ret=0
        for y in range(N):
            for x in range(N):
                ret=max(ret,dp[y][x])
        return ret

class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        # brute force
        record={}
        for y,x in mines:
            record[(y,x)]=1
        ret=0
        for y in range(N):
            for x in range(N):
                if (y,x) not in record:
                    offset=0
                    while True:
                        offset+=1
                        cnt=0
                        for y0,x0 in [(y-offset,x),(y+offset,x),(y,x-offset),(y,x+offset)]:
                            if (y0,x0) in record or y0<0 or y0>=N or x0<0 or x0>=N:
                                cnt+=1
                        if cnt>0:
                            break
                    ret=max(offset,ret)
        return ret