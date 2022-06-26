class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        s1=sum(nums1)
        s2=sum(nums2)
        def check(lst0,lst1):
            lst=[a-b for a,b in zip(lst0,lst1)]
            acc=0
            cur=0
            for i in range(len(lst)):
                acc=max(lst[i],acc+lst[i],0)
                cur=max(acc,cur)
            return cur
        return max(s1,s2,check(nums1,nums2)+s2,check(nums2,nums1)+s1)