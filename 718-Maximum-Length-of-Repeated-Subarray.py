class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        ret=0
        template=[0]*(len(nums2)+1)
        dp=[template[:] for _ in range(len(nums1)+1)]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    dp[i][j]=max(dp[i][j],dp[i-1][j-1]+1)
                ret=max(dp[i][j],ret)
        return ret