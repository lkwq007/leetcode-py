class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # 1 <= nums.length <= 1000
        record={}
        ret=0
        dp=[{} for _ in range(len(nums))]
        for i in range(len(nums)):
            record=dp[i]
            for j in range(i+1,len(nums)):
                diff=nums[j]-nums[i]
                if diff in record:
                    ret+=record[diff]
                dp[j][diff]=dp[j].get(diff,0)+record.get(diff,0)+1
        # print(record)
        # print(dp)
        return ret
