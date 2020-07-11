class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        record={}
        for item in nums1:
            record[item]=1
        ret=[]
        for item in nums2:
            if record.get(item,0)==1:
                ret.append(item)
                record[item]=2
        return ret