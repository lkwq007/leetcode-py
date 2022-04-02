class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # brute force
        lst=[item for item in nums if item>0]
        nums=lst
        m=min(len(nums),m)
        if len(nums)<1:
            return 0
        prefix=[0]*(len(nums)+1)
        for i in range(len(nums)):
            prefix[i]=nums[i]+prefix[i-1]
        dp=[[prefix[-2]]*len(nums) for _ in range(m)]
        for i in range(len(nums)):
            for j in range(m):
                if j==0:
                    dp[j][i]=prefix[i]
                else:
                    left=0
                    right=i-1
                    # find peak
                    while left<right:
                        middle=left+(right-left)//2
                        val0=max(dp[j-1][middle],prefix[i]-prefix[middle])
                        val1=max(dp[j-1][middle+1],prefix[i]-prefix[middle+1])
                        if val0>val1:
                            left=middle+1
                        else:
                            right=middle
                    dp[j][i]=min(max(dp[j-1][left],prefix[i]-prefix[left]),dp[j][i])
        return dp[-1][-1]

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # brute force tle
        lst=[item for item in nums if item>0]
        nums=lst
        m=min(len(nums),m)
        if len(nums)<1:
            return 0
        prefix=[0]*(len(nums)+1)
        for i in range(len(nums)):
            prefix[i]=nums[i]+prefix[i-1]
        dp=[[prefix[-2]]*len(nums) for _ in range(m)]
        for i in range(len(nums)):
            for j in range(m):
                if j==0:
                    dp[j][i]=prefix[i]
                else:
                    for k in range(i):
                        dp[j][i]=min(max(dp[j-1][k],prefix[i]-prefix[k]),dp[j][i])
        return dp[-1][-1]