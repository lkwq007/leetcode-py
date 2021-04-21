class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=[0]*(target+1)
        for item in nums:
            if item<=target:
                dp[item]+=1
        for i in range(1,target+1):
            for item in nums:
                dp[i]+=dp[max(0,i-item)]
        return dp[-1]