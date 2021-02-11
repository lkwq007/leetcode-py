class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # O(N^2)
        dp=[1]*len(nums)
        ret=1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    dp[j]=max(dp[j],dp[i]+1)
                ret=max(ret,dp[j])
        return ret

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # O(NLogN)?
        dp=[]
        for item in nums:
            left=0
            right=len(dp)
            while left<right:
                middle=left+(right-left)//2
                if dp[middle]==item:
                    left=middle
                    break
                elif dp[middle]<item:
                    left=middle+1
                else:
                    right=middle
            if left==len(dp):
                dp.append(item)
            else:
                dp[left]=item
        return len(dp)