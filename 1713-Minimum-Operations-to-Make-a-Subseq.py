# class Solution:
#     def minOperations(self, target: List[int], arr: List[int]) -> int:
#         # brute force TLE
#         template=[0]*(len(arr)+1)
#         dp=[template[:] for _ in range(len(target)+1)]
#         ret=0
#         for i in range(1,len(target)+1):
#             for j in range(1,len(arr)+1):
#                 if target[i-1]==arr[j-1]:
#                     dp[i][j]=max(dp[i-1][j-1]+1,dp[i][j-1],dp[i-1][j])
#                 else:
#                     dp[i][j]=max(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])
#                 ret=max(dp[i][j],ret)
#         return len(target)-ret

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        # LIS
        record={}
        for i,item in enumerate(target):
            record[item]=i
        lst=[record[item] for item in arr if item in record]
        dp=[]
        for item in lst:
            left=0
            right=len(dp)
            while left<right:
                middle=left+(right-left)//2
                if dp[middle]==item:
                    left=middle
                    break
                elif dp[middle]<item:
                    left=middle+1
                else:
                    right=middle
            if left==len(dp):
                dp.append(item)
            else:
                dp[left]=item
        return len(target)-len(dp)