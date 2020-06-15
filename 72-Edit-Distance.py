class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1=len(word1)
        len2=len(word2)
        if len1<1 or len2<1:
            return max(len1,len2)
        # optimal alignment
        template=[0]*(len2+1)
        dp=[template[:] for _ in range(len1+1)]
        for i in range(1,len1+1):
            dp[i][0]=i
        for j in range(1,len2+1):
            dp[0][j]=j
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                cur=0 if word1[i-1]==word2[j-1] else 1
                dp[i][j]=min(dp[i-1][j-1]+cur,dp[i-1][j]+1,dp[i][j-1]+1)
        return dp[-1][-1]

# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         len1=len(word1)
#         len2=len(word2)
#         if len1<1 or len2<1:
#             return max(len1,len2)
#         template=[0]*(len2+1)
#         dp=[template[:] for _ in range(0,len1+1)]
#         for i in range(1,len1+1):
#             for j in range(1,len2+1):
#                 # i,j are offseted by 1
#                 cur=1 if word1[i-1]==word2[j-1] else 0
#                 dp[i][j]=max(dp[i-1][j-1]+cur,dp[i-1][j],dp[i][j-1])
#         i=len1
#         j=len2
#         cross=dp[-1][-1]
#         lst=[]
#         while i>=1 and j>=1:
#             while i>1 and dp[i-1][j]==dp[i][j]:
#                 i-=1
#             while j>1 and dp[i][j-1]==dp[i][j]:
#                 if word1[i-1]==word2[j-1]:
#                     break
#                 j-=1
#             if dp[i][j]>0:
#                 lst.append([i-1,j-1])
#             i-=1
#             j-=1
#         deleted=len1-cross
#         ptr1=0
#         ptr2=0
#         acc=0
#         lst=lst[::-1]
#         for a,b in lst:
#             deleted=a-ptr1
#             inserted=b-ptr2
#             acc+=max(inserted,deleted)
#             ptr1=a+1
#             ptr2=b+1
#         acc+=max(len1-ptr1,len2-ptr2)
#         return acc



                    

x=Solution()
print(x.minDistance("horse","ros"))
print(x.minDistance("mart","karma"))

