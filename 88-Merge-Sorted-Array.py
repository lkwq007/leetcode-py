class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(1,m+1):
            nums1[-i]=nums1[m-i]
        pos1=len(nums1)-m
        pos2=0
        cur=0
        total1=len(nums1)
        total2=len(nums2)
        while pos1<total1 and pos2<total2:
            if nums1[pos1]<nums2[pos2]:
                nums1[cur]=nums1[pos1]
                pos1+=1
            else:
                nums1[cur]=nums2[pos2]
                pos2+=1
            cur+=1
        while pos2<total2:
            nums1[cur]=nums2[pos2]
            cur+=1
            pos2+=1
        while pos1<total1:
            return
            