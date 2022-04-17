class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        middle=(len(nums1)+len(nums2)-1)//2
        def find(k,l1,r1,l2,r2):
            # print(k,l1,r1,l2,r2)
            len1=r1-l1+1
            len2=r2-l2+1
            def val1(idx):
                return nums1[l1+idx]
            def val2(idx):
                return nums2[l2+idx]
            if len1<1:
                return val2(k)
            elif len2<1:
                return val1(k)
            if val1(len1-1)<=val2(0):
                return val1(k) if k<len1 else val2(k-len1)
            elif val2(len2-1)<=val1(0):
                return val2(k) if k<len2 else val1(k-len2)
            # overlap
            m1=(len1-1)//2
            m2=(len2-1)//2
            # middle point should be removed
            if val1(m1)<=val2(0):
                return val1(k) if k<=m1 else find(k-m1-1,l1+m1+1,r1,l2,r2)
            elif val1(m1)>=val2(len2-1):
                if k<len2+m1:
                    return find(k,l1,l1+m1-1,l2,r2)
                else:
                    return val1(k-len2)
            else:
                if val1(m1)<=val2(m2):
                    if k<m1+m2+1:
                        return find(k,l1,r1,l2,l2+m2-1)
                    else:
                        return find(k-m1-1,l1+m1+1,r1,l2,r2)
                else:
                    if k<m1+m2+1:
                        return find(k,l1,l1+m1-1,l2,r2)
                    else:
                        return find(k-m2-1,l1,r1,l2+m2+1,r2)
        if (len(nums1)+len(nums2))%2:
            return find(middle,0,len(nums1)-1,0,len(nums2)-1)
        return (find(middle,0,len(nums1)-1,0,len(nums2)-1)+find(middle+1,0,len(nums1)-1,0,len(nums2)-1))/2