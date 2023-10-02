class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # 1 <= nums[i] <= 10^6
        right_max=nums[:]
        dp=[0]*len(nums)
        left_max=nums[:]
        for i in range(len(nums)-2,-1,-1):
            right_max[i]=max(right_max[i+1],nums[i])
        for i in range(1,len(nums)):
            left_max[i]=max(left_max[i-1],nums[i])
        dp[1]=max(0,nums[0]-nums[1])
        ret=0
        for i in range(2,len(nums)):
            # max diff before i
            dp[i]=max(dp[i-1],left_max[i-1]-nums[i])
            ret=max(dp[i-1]*right_max[i],ret)
        return ret
        