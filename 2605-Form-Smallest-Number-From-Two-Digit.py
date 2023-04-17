class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        a=min(nums1)        
        b=min(nums2)
        ret=set(nums1).intersection(set(nums2))
        ret.add(100)
        return min(a*10+b,b*10+a,min(ret))