class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # TLE
        dp=[None]*len(nums)
        dp[0]=nums[0]
        for i in range(len(nums)):
            for j in range(i+1,min(len(nums),i+k+1)):
                if dp[j] is None:
                    dp[j]=dp[i]+nums[j]
                else:
                    dp[j]=max(dp[j],dp[i]+nums[j])
        return dp[-1]
