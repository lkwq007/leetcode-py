class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # brute force
        dp=[[1]*len(nums),[1]*len(nums)]
        ret=1
        for i in range(len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[0][i]=max(dp[0][i],1+dp[1][j])
                elif nums[j]>nums[i]:
                    dp[1][i]=max(dp[1][i],1+dp[0][j])