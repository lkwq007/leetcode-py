class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp=[[0 for _ in range(len(rods))] for _ in range(2501)]
        rods.sort()
        total=sum(rods)
        ret=0
        for i in range(len(rods)):
            dp[rods[i]][i]+=1
            for j in range(i):
                for k in range(total):
                    if dp[k][j]>0:
                        dp[k+rods[i]][i]=max(dp[k+rods[i]][i],dp[k][j])
        print(dp[100:])
        return ret


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

