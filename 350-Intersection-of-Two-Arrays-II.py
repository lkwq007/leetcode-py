class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst=[0]*1001
        for item in nums1:
            lst[item]+=1
        ret=[]
        for item in nums2:
            lst[item]-=1
            if lst[item]>=0:
                ret.append(item)
        return ret
# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         lst1=[0]*1001
#         lst2=[0]*1001
#         for item in nums1:
#             lst1[item]+=1
#         for item in nums2:
#             lst2[item]+=1
#         ret=[]
#         for i in range(len(lst1)):
#             val=min(lst1[i],lst2[i])
#             for _ in range(val):
#                 ret.append(i)
#         return ret