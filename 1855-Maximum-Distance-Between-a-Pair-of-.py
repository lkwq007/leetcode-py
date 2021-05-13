class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        idx1=len(nums1)-1
        idx2=len(nums2)-1
        ret=0
        for idx1 in range(len(nums1)-1,-1,-1):
            while idx2>=idx1 and nums1[idx1]>nums2[idx2]:
                idx2-=1
            ret=max(ret,idx2-idx1)
        return ret