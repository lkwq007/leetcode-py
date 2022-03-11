class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        term=10**9+7
        dp=[0]*3
        for i in range(len(nums)):
            item=int(nums[i])
            dp[item]=2*dp[item]+(1 if item==0 else dp[item-1])
            dp[item]%=term
        return dp[-1]

class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        return reduce(lambda acc,x:[acc[i]%(10**9+7) if i!=x else (2*acc[x]+(1 if x==0 else acc[x-1]))%(10**9+7) for i in range(3)], map(int,nums), (0,0,0))[-1]