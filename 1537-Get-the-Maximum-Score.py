class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        dp1=[0]*(1+len(nums1))
        dp2=[0]*(1+len(nums2))
        i=0
        j=0
        ret=0
        term=10**9+7
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                dp1[i]=dp1[i-1]+nums1[i]
                i+=1
            elif nums1[i]>nums2[j]:
                dp2[j]=dp2[j-1]+nums2[j]
                j+=1
            else:
                dp1[i]=max(dp1[i-1]+nums1[i],dp2[j-1]+nums1[i])
                dp2[j]=max(dp2[j-1]+nums2[j],dp1[i-1]+nums2[j])
                i+=1
                j+=1
        while i<len(nums1):
            dp1[i]=dp1[i-1]+nums1[i]
            i+=1
        while j<len(nums2):
            dp2[j]=dp2[j-1]+nums2[j]
            j+=1
        return max(dp1[-2],dp2[-2])%term
