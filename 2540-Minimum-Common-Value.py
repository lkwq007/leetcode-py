class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        idx0=0
        idx1=0
        while idx0<len(nums1) and idx1<len(nums2):
            if nums1[idx0]==nums2[idx1]:
                return nums1[idx0]
            elif nums1[idx0]<nums2[idx1]:
                idx0+=1
            else:
                idx1+=1
        return -1