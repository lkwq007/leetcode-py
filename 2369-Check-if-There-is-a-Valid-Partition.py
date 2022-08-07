class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp=[0]*(len(nums)+1)
        dp[-1]=1
        if nums[1]==nums[0]:
            dp[1]=1
        for i in range(2,len(nums)):
            if nums[i]==nums[i-1] and dp[i-2]==1:
                dp[i]=1
            if nums[i]==nums[i-1]==nums[i-2] and dp[i-3]==1:
                dp[i]=1
            if nums[i-2]+1==nums[i-1] and nums[i-1]+1==nums[i] and dp[i-3]==1:
                dp[i]=1
        return dp[-2]==1

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp=[0]*(len(nums)+1)
        dp[-1]=1
        if nums[1]==nums[0]:
            dp[1]=1
        for i in range(2,len(nums)):
            if nums[i]==nums[i-1] and dp[i-2]==1 or \
                nums[i]==nums[i-1]==nums[i-2] and dp[i-3]==1 or \
                nums[i-2]+1==nums[i-1] and nums[i-1]+1==nums[i] and dp[i-3]==1:
                dp[i]=1
        return dp[-2]==1
