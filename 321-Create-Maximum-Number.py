class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        idx1=0
        idx2=0
        ret=[]
        for i in range(k):
            if idx1<len(nums1) and idx2<len(nums2):
                if nums1[idx1]>nums2[idx2]:
                    ret.append(nums1[idx1])
                    idx1+=1
                elif nums1[idx1]<nums2[idx2]:
                    ret.append(nums2[idx2])
                    idx2+=1
                else:
                    ret.append(nums1[idx1])
                    if idx1+1<len(nums1) and idx2+1<len(nums2):
                        if nums1[idx1+1]<nums2[idx2+1]:
                            idx2+=1
                        else:
                            idx1+=1
            elif idx1<len(nums1):
                ret.append(nums1[idx1])
                idx1+=1
            elif idx2<len(nums2):
                ret.append(nums2[idx2])
                idx2+=1
        return ret