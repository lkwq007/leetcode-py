# class Solution:
#     def numSquares(self, n: int) -> int:
#         import math
#         count=0
#         while n>0:
#             part=int(math.sqrt(n))
#             n-=part*part
#             count+=1
#         return count
# class Solution:
#     def numSquares(self, n: int) -> int:
#         factor=[]
#         i=1
#         while i*i<=n:
#             factor.append(i*i)
#             i+=1
#         if factor[-1]*factor[-1]==n:
#             return 1
#         dp=[-1]*(n+1)
#         for item in factor:
#             dp[item]=1
#         def squares(n,rightmost):
#             if dp[n]>0:
#                 return dp[n]
#             if rightmost==0:
#                 return n
#             cnt=n
#             for idx in range(rightmost,-1,-1):
#                 if factor[idx]>n:
#                     continue
#                 elif factor[idx]==n:
#                     dp[n]=1
#                     return 1
#                 else:
#                     cnt=min(cnt,1+squares(n-factor[idx],idx))
#             dp[n]=cnt
#             return cnt
#         return squares(n,len(factor)-1)
class Solution:
    def numSquares(self, n: int) -> int:
        factor=[]
        i=1
        while i*i<=n:
            factor.append(i*i)
            i+=1
        if factor[-1]*factor[-1]==n:
            return 1
        dp=[-1]*(n+1)
        for item in factor:
            dp[item]=1
        def squares(n,rightmost):
            if dp[n]>0:
                return dp[n]
            cnt=n
            tmp=rightmost
            for idx in range(rightmost,-1,-1):
                if factor[idx]>n:
                    tmp=idx-1
                    continue
                elif factor[idx]==n:
                    dp[n]=1
                    return 1
                else:
                    cnt=min(cnt,1+squares(n-factor[idx],tmp))
            dp[n]=cnt
            return cnt
        return squares(n,len(factor)-1)
x=Solution()
print(x.numSquares(1000))
