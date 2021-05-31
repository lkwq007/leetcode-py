
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        # TLE
        total=sum(rods)
        template=[False]*(len(rods)+1)
        dp=[template[:] for _ in range(total*4+1)]
        template=[0]*(len(rods)+1)
        ret=[template[:] for _ in range(total*4+1)]
        dp[total][0]=True
        # dp[i][j] first i sum == j-total
        for i in range(len(rods)):
            for j in range(total*2+1):
                dp[j][i+1]=dp[j][i] or dp[j+rods[i]][i] or dp[j-rods[i]][i]
                if dp[j][i]:
                    ret[j][i+1]=max(ret[j][i],ret[j][i+1])
                if dp[j+rods[i]][i]:
                    ret[j][i+1]=max(ret[j+rods[i]][i],ret[j][i+1])
                if dp[j-rods[i]][i]:
                    ret[j][i+1]=max(ret[j-rods[i]][i]+rods[i],ret[j][i+1])
        return ret[total][-1]


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        # TLE
        total=sum(rods)
        template=[False]*(total*4+1)
        dp=[template[:] for _ in range(len(rods)+1)]
        template=[0]*(total*4+1)
        ret=[template[:] for _ in range(len(rods)+1)]
        dp[0][total]=True
        # dp[i][j] first i sum == j-total
        for i in range(len(rods)):
            for j in range(total*2+1):
                dp[i+1][j]=dp[i][j] or dp[i][j+rods[i]] or dp[i][j-rods[i]]
                if dp[i][j]:
                    ret[i+1][j]=max(ret[i][j],ret[i+1][j])
                if dp[i][j+rods[i]]:
                    ret[i+1][j]=max(ret[i][j+rods[i]],ret[i+1][j])
                if dp[i][j-rods[i]]:
                    ret[i+1][j]=max(ret[i][j-rods[i]]+rods[i],ret[i+1][j])
        return ret[-1][total]


# class Solution:
#     def tallestBillboard(self, rods: List[int]) -> int:
#         dp=[set([]) for _ in range(2501)]
#         mask=1
#         for item in rods:
#             dp[item].add(mask)
#             mask=mask<<1
#         ret=0
#         def count(idx):
#             lst=list(dp[idx])
#             for i in range(len(lst)):
#                 for j in range(i+1,len(lst)):
#                     if lst[i]&lst[j]==0:
#                         return True
#             return False
#         total=sum(rods)
#         for i in range(1,total):
#             for j in range(1,i):
#                 for x in dp[j]:
#                     for y in dp[i-j]:
#                         if x&y==0:
#                             flag=True
#                             for val in dp[i]:
#                                 if (x|y)&val!=0:
#                                     flag=False
#                                     break
#                             if flag:
#                                 dp[i].add(x|y)
#             if len(dp[i])>1:
#                 ret=i
#         return ret

# class Solution:
#     def tallestBillboard(self, rods: List[int]) -> int:
#         dp=[set([]) for _ in range(2501)]
#         mask=1
#         for item in rods:
#             dp[item].add(mask)
#             mask=mask<<1
#         ret=0
#         def count(idx):
#             lst=list(dp[idx])
#             for i in range(len(lst)):
#                 for j in range(i+1,len(lst)):
#                     if lst[i]&lst[j]==0:
#                         return True
#             return False
#         total=sum(rods)
#         for i in range(1,total):
#             for j in range(1,i):
#                 for x in dp[j]:
#                     for y in dp[i-j]:
#                         if x&y==0:
#                             dp[i].add(x|y)
#             if count(i):
#                 ret=i
#         return ret

