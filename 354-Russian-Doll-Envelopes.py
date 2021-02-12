class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if len(envelopes)<2:
            return len(envelopes)
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        dp=[]
        for w,h in envelopes:
            left=0
            right=len(dp)
            while left<right:
                middle=left+(right-left)//2
                if dp[middle]==h:
                    left=middle
                    break
                elif dp[middle]<h:
                    left=middle+1
                else:
                    right=middle
            if len(dp)==left:
                dp.append(h)
            else:
                dp[left]=h
        return len(dp)

# class Solution:
#     def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
#         if len(envelopes)<2:
#             return len(envelopes)
#         envelopes.sort(key=lambda x:(x[0],x[1]))
#         # brute force TLE
#         total=len(envelopes)
#         dp=[1]*total
#         ret=1
#         for i in range(total):
#             for j in range(i+1,total):
#                 if envelopes[j][0]>envelopes[i][0] and envelopes[j][1]>envelopes[i][1]:
#                     dp[j]=max(dp[j],dp[i]+1)
#                 ret=max(ret,dp[j])
#         return ret