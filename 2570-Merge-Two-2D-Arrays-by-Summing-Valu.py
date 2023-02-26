class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        idx1=0
        idx2=0
        ret=[]
        while idx1<len(nums1) or idx2<len(nums2):
            i1,v1=nums1[idx1] if idx1<len(nums1) else (1001,0)
            i2,v2=nums2[idx2] if idx2<len(nums2) else (1001,0)
            if i1<i2:
                ret.append([i1,v1])
                idx1+=1
            elif i1==i2:
                ret.append([i1,v1+v2])
                idx1+=1
                idx2+=1
            else:
                ret.append([i2,v2])
                idx2+=1
        return ret
            