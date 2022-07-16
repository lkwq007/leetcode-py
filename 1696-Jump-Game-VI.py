from collections import deque
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # I am stupid
        queue=deque([(nums[0],0)],maxlen=k)
        # max sliding windows
        for i in range(1,len(nums)):
            cur=queue[0][0]+nums[i]
            while queue and queue[-1][0]<cur:
                queue.pop()
            queue.append((cur,i))
            while queue and queue[0][1]<=i-k:
                queue.popleft()
        return queue[-1][0]




# class Solution:
#     def maxResult(self, nums: List[int], k: int) -> int:
#         # TLE
#         lst=[]
#         acc=nums[0]
#         cnt=1
#         for i in range(1,len(nums)):
#             if nums[i]>=0 or i==len(nums)-1:
#                 acc+=nums[i]
#                 if cnt>k:
#                     lst.append((i-cnt,i))
#                 cnt=1
#             else:
#                 cnt+=1
#         def probe(start,end):
#             total=end-start+1
#             dp=[None]*(end-start+1)
#             dp[0]=0
#             for i in range(total):
#                 for j in range(i+1,min(total,i+k+1)):
#                     if dp[j] is None:
#                         dp[j]=dp[i]+nums[start+j]
#                     else:
#                         dp[j]=max(dp[j],dp[i]+nums[start+j])
#             return dp[-1]-nums[end]
#         for start,end in lst:
#             acc+=probe(start,end)
#         return acc


# class Solution:
#     def maxResult(self, nums: List[int], k: int) -> int:
#         # TLE
#         dp=[None]*len(nums)
#         dp[0]=nums[0]
#         for i in range(len(nums)):
#             for j in range(i+1,min(len(nums),i+k+1)):
#                 if dp[j] is None:
#                     dp[j]=dp[i]+nums[j]
#                 else:
#                     dp[j]=max(dp[j],dp[i]+nums[j])
#         return dp[-1]
