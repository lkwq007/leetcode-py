class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1s={}
        nums2s={}
        for item in nums1:
            tmp=item*item
            nums1s[tmp]=nums1s.get(tmp,0)+1
        for item in nums2:
            tmp=item*item
            nums2s[tmp]=nums2s.get(tmp,0)+1
        ret=0
        for i in range(len(nums1)):
            for j in range(i):
                tmp=nums1[i]*nums1[j]
                ret+=nums2s.get(tmp,0)
        for i in range(len(nums2)):
            for j in range(i):
                tmp=nums2[i]*nums2[j]
                ret+=nums1s.get(tmp,0)
        return ret