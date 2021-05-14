class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        size=len(board)
        dp=[]
        term=10**9+7
        for i in range(size):
            dp.append([[0,0] for _ in range(size)])
        dp[-1][-1][1]=1
        for x in range(size-2,-1,-1):
            if board[-1][x]!="X":
                tmp=int(board[-1][x])
                dp[-1][x][0]=dp[-1][x+1][0]+tmp
                dp[-1][x][1]=dp[-1][x+1][1]
            if board[x][-1]!="X":
                tmp=int(board[x][-1])
                dp[x][-1][0]=dp[x+1][-1][0]+tmp
                dp[x][-1][1]=dp[x+1][-1][1]
        for y in range(size-2,-1,-1):
            for x in range(size-2,-1,-1):
                if board[y][x]!="X":
                    tmp=int(board[y][x]) if board[y][x]!="E" else 0
                    for k,v in [dp[y+1][x],dp[y][x+1],dp[y+1][x+1]]:
                        if dp[y][x][0]<k+tmp:
                            dp[y][x][0]=k+tmp
                            dp[y][x][1]=v
                        elif dp[y][x][0]==k+tmp:
                            dp[y][x][1]+=v
                        dp[y][x][1]%=term
        return dp[0][0] if dp[0][0][-1]>0 else [0,0]


# I am stupid
# import itertools
# class Solution:
#     def pathsWithMaxScore(self, board: List[str]) -> List[int]:
#         size=len(board)
#         dp=[]
#         term=10**9+7
#         for i in range(size):
#             dp.append([{} for _ in range(size)])
#         dp[-1][-1][0]=1
#         for x in range(size-2,-1,-1):
#             if board[-1][x]!="X":
#                 tmp=int(board[-1][x])
#                 for k,v in dp[-1][x+1].items():
#                     dp[-1][x][k+tmp]=v
#             if board[x][-1]!="X":
#                 tmp=int(board[x][-1])
#                 for k,v in dp[x+1][-1].items():
#                     dp[x][-1][k+tmp]=v
#         for y in range(size-2,-1,-1):
#             for x in range(size-2,-1,-1):
#                 if board[y][x]!="X":
#                     tmp=int(board[y][x]) if board[y][x]!="E" else 0
#                     record=dp[y][x]
#                     for k,v in itertools.chain(dp[y+1][x].items(),dp[y][x+1].items(),dp[y+1][x+1].items()):
#                         record[k+tmp]=(record.get(k+tmp,0)+v)%term
#                     dp[y][x]=record
#         return [0,0] if len(dp[0][0])==0 else [max(dp[0][0]),dp[0][0][max(dp[0][0])]]