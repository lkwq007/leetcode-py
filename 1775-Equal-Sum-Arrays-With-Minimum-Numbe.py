class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        min1,min2=len(nums1),len(nums2)
        max1,max2=min1*6,min2*6
        if min1>max2 or min2>max1:
            return -1
        lst1=[0]*7
        lst2=[0]*7
        for item in nums1:
            lst1[item]+=1
        for item in nums2:
            lst2[item]+=1
        for i in range(7):
            val=min(lst1[i],lst2[i])
            lst1[i]-=val
            lst2[i]-=val
        return sum(lst1)