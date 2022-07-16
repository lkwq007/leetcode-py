class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        dp=[0]*(len(nums)+1)
        record={0:-1}
        prefix=[0]*len(nums)
        for i in range(len(nums)):
            prefix[i]=prefix[i-1]+nums[i]
            val=prefix[i]
            rest=val-target
            if rest in record:
                dp[i]=max(dp[i-1],1+dp[record[rest]])
            else:
                dp[i]=dp[i-1]
            record[val]=i
        return dp[-2]